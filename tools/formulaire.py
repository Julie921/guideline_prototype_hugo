import streamlit as st
import pandas as pd
from create_request_from_json import create_request_file
from json2md import add_link,json_to_markdown_no_pattern,json_to_markdown_fwith_pattern
from test_build_table import process_files
import os 
from write_in_file import add_text, parcourir_arborescence, check_env, add_text_check, read_partial_markdown
from streamlit_extras.stoggle import stoggle
from streamlit_extras.mention import mention


st.title("Formular to help the guideline's writting")

st.markdown("""
This script is a form to guide the user in writing the annotation guide. It corresponds to the annotation guide formalism established in my thesis. The rest of the script allows for automatic saving and updating of the annotation guide. It also enables the creation of direct pattern-to-table mappings in the section where patterns can be specified. If a question is not indicated as optional, it is because it is required for writing the MD page.

:warning: :red[WARNING: The language provided must match the language present in the annotation guide file and sub-files in the tools folder.] See README.md :warning:

""")

from streamlit_extras.echo_expander import echo_expander



liste_of_upos = ['AUX','ADV','DET','VERB','SYM','X','CCONJ','SCONJ','ADJ','PRON','PROPN','INTJ','ADP','NUM','PART','PUNCT','NOUN']
list_of_deprel = ['comp','comp:aux','comp:pred','comp:obj',"comp:obl","comp:cleft","compound","conj","conj:appos","conj:coord","conj:dicto","det","discourse","dislocated","flat","parataxis","parataxis:obj","parataxis:insert","punct","root","subj","udep","unk","cc","vocative"]
list_of_deep = ["pass","relcl","tense","x","caus","name","agent","emb","lvc","foreign","expl"]
particular_phenomena_check = ['numeral','coordination','comparative_construction','disfluency','reported_speech']
liste_of_features=["Number","Gender","Mood","Person","Polarity","Tense","VerbForm","Shared","Subject"]
liste_of_misc=["CorrectForm","ExtPos","Idiom_Titles","Typo","Reported","Word_TextForm"]

def add_answer():
    """
    This function creates input fields for the name, pattern, description, and example of an answer (when creating a pattern description). 
    If the user clicks the "Add" button, the entered data is stored in a list of answers stored in the session of the Streamlit application.
    """
    # get the answer's list for the session. Can be empty. 
    answers = st.session_state.get('answers', [])

    # texts zone for the answers
    name = st.text_input("Name")
    pattern = st.text_input('Pattern')
    descr = st.text_area('Description',height=200)
    example = st.text_area('Example (conll)',height=200)

    # if we click the Ajouter button, we add the answer in the list "answers"
    if st.button('Ajouter'):
        answers.append({'name':name,'description': descr, 'pattern': pattern, 'example':example})
        st.success('Pattern added successfully! You can add another one')
        name = st.empty() # réinitialisation des champs de texte
        pattern = st.empty()
        descr = st.empty()
        example = st.empty()
    # update the list of answers during the session. 
    st.session_state.answers = answers


st.title("Begining of the script")

# Formular -> different question for each tag

# Get the language
language = st.text_input('Name of the language')



# Get the type of page that the user want to write. 
tag = st.radio("What do you want to documentate ? ", ('Syntactic relation','Morphological features','Lexical features','Part of Speech','Other linguistic phenomena','Deep relation tag','Universal construction'))


##################################################################################
######################## PARTICULAR CONSTRUCTION #################################
##################################################################################
## particular construction -> as define in the guideline ! If it exist, we cannot create an "other linguistic phenomena"
if tag == 'Universal construction':

    tag = 'Universal_construction'
    # which particular construction 
    which_phenm = st.multiselect(f'wich particular construction do you want to documente in your language ?', particular_phenomena_check)

    which_phenm_str = ", ".join(which_phenm)
    if which_phenm:
        explaination = read_partial_markdown(f"../content/docs/general_guideline/{tag}/{which_phenm_str}.md")

        with st.expander(f"See explanation of {which_phenm_str}"):
            

            mention(
                label="See the guidelines page for more",
                icon="streamlit",  # Some icons are available... like Streamlit!
                url=f"https://julie921.github.io/guideline_prototype_hugo/docs/general_guideline/Universal_construction/{which_phenm_str}/",
            )
            st.write(f"""
                {explaination}
        """)
    # description
    overview = st.text_area(f"Can you give a short description of the feature {which_phenm} in your language ? ", height=200) 

    # give general example
    general_ex = st.text_area(f"Conll example",height=200)

    # THe user can add some pattern to describe in his page 
    add_pattern = st.radio("Du you want to describe some specifs patterns ? ",('Yes','No'))
    if add_pattern == "Yes":
        st.write("Describe your pattern")
        add_answer()
    get_pattern = {}
    # we get the information from the function and put them in a dict 
    for answer in st.session_state.answers:
        get_pattern[answer["name"]]={'pattern':answer["pattern"], 'descriptions':answer["description"], 'example':answer['example']}

    # Add the data in a DataFrame
    data = {'Language': [language], 'Tag': [tag],'value': [which_phenm],'overview':[overview], 'general_ex':[general_ex],'upos_and_value_feats':[dict()],'specific_pattern':[get_pattern]}
    df = pd.DataFrame(data)

##################################################################################
######################## FEATS AND Miscs##########################################
##################################################################################

# Different type of page
if tag == 'Morphological features' or tag =="Lexical features":
    """
    Text zone to write the a Feature's or Misc's page for the guideline. 
    """

    # dict to get the upos that can have the features? 
    upos_value = {}

    # name of the features
    if tag =='Morphological features':
        tag = 'Features'
        feats = st.multiselect(f'Choose the features ?', liste_of_features)
    if tag =="Lexical features":
        tag = "MISC"
        feats = st.multiselect(f'Choose the features ?', liste_of_misc)

    if len(feats) == 1:
        feats = str(feats[0])

        # short description of the features
        overview = st.text_area(f"Can you give a short description of the feature {feats} in your language ? ", height=200) 

        # give general example
        general_ex = st.text_area(f"Conll example",height=200)
        
        # which upos can have the features 
        which_upos = st.multiselect(f'which upos are conserned by the feature {feats} ? (optional)', liste_of_upos)

        # for each upos, we can indicates the feature's value 
        for i in range(len(which_upos)):
            combo_value_feats = st.text_input(f"Which are the value of the features {feats} for the upos {which_upos[i]} ? (put a ';' between each value)")
            combos = combo_value_feats.split(";")
            upos_value[which_upos[i]] = combos
        
        # THe user can add some pattern to describe in his page 
        add_pattern = st.radio("Du you want to describe some specifs patterns ? ",('Yes','No'))
        if add_pattern == "Yes":
            st.write("Describe your pattern")
            add_answer()
        get_pattern = {}
        # we get the information from the function and put them in a dict 
        for answer in st.session_state.answers:
            get_pattern[answer["name"]]={'pattern':answer["pattern"], 'descriptions':answer["description"], 'example':answer['example']}

        # Add the data in a DataFrame
        data = {'Language': [language], 'Tag': [tag],'value': [feats],'overview':[overview], 'general_ex':[general_ex],'upos_and_value_feats':[upos_value] ,'specific_pattern':[get_pattern]}
        df = pd.DataFrame(data)
    
    if len(feats) > 1:
        st.write("Choose only one tag!")


##################################################################################
#################################### UPOS ########################################
##################################################################################
# Different type of page
if tag == 'Part of Speech':

    tag = "Upos"

    # dict to get the feats that can be on the upos
    features_name = {}

    # name of the features
    upos = st.multiselect(f'Choose the features ?', liste_of_upos)

    if len(upos)==1:
        upos = str(upos[0])

        # short description of the features
        overview = st.text_area(f"Can you give a short description of the feature {upos} in your language ? ", height=200) 

        # give general example
        general_ex = st.text_area(f"Conll example",height=200)

        # which upos can have the features 
        which_features = st.text_area(f"Which features can be on the {upos} ? (put a ';' between each value) (optional)",height=10)

        which_features = which_features.split(";")

        # for each features, we can indicates the feature's value 
        for i in range(len(which_features)):
            combo_value_feats = st.text_input(f"Which are the value of the features {which_features[i]} for the upos {upos} ? (put a ';' between each value)")
            combos = combo_value_feats.split(";")
            features_name[which_features[i]] = combos
        
        # THe user can add some pattern to describe in his page 
        add_pattern = st.radio("Du you want to describe some specifs patterns ? ",('Yes','No'))
        if add_pattern == "Yes":
            st.write("Describe your pattern")
            # fonction add_answer()
            add_answer()
        get_pattern = {}
        # we get the information from the function and put them in a dict 
        for answer in st.session_state.answers:
            get_pattern[answer["name"]]={'pattern':answer["pattern"], 'descriptions':answer["description"], 'example':answer['example']}

        # Add the data in a DataFrame
        data = {'Language': [language], 'Tag': [tag],'value': [upos],'overview':[overview], 'general_ex':[general_ex],'upos_and_value_feats':[features_name] ,'specific_pattern':[get_pattern]}
        df = pd.DataFrame(data)
    
    if len(upos) > 1:
        st.write("Choose only one tag !")

##################################################################################
######################## Syntactic relations  ####################################
##################################################################################

# Different type of page
if tag == 'Syntactic relation' or tag == 'Deep relation tag':
    """
    Text zone to write the a syntactic relation's page for the guideline. 
    """

    # dict to get the upos that can have the features? 
    upos_value = {}
    
    # name of the features
    if tag =='Syntactic relation':
        tag = 'Syntactic_relations'
        deprel = st.multiselect(f'Choose the features ?', list_of_deprel)
    if tag =="Deep relation tag":
        tag = "Deep"
        deprel = st.multiselect(f'Choose the features ?', list_of_deep)

    if len(deprel) == 1:

        deprel = str(deprel[0])

        deprel = deprel.replace(":","_")

        # short description of the features
        overview = st.text_area(f"Can you give a short description of the feature {deprel} in your language ? ",height=200) 
        
        # give general example
        general_ex = st.text_area(f"Conll example",height=200)

        # which upos can have the features 
        which_upos = st.multiselect(f'which upos can be the head of the {deprel} ? (optional)', liste_of_upos)

        # for each upos, we can indicates the feature's value 
        for i in range(len(which_upos)):
            combo_value_feats = st.multiselect(f"For this {which_upos[i]}, what can be the dependent of the {deprel} ?", liste_of_upos)
            combos = combo_value_feats
            upos_value[which_upos[i]] = combos
        
        # THe user can add some pattern to describe in his page 
        add_pattern = st.radio("Du you want to describe some specifs patterns ? ",('Yes','No'))
        if add_pattern == "Yes":
            st.write("Describe your pattern")
            # fonction add_answer()
            add_answer()
        get_pattern = {}
        # we get the information from the function and put them in a dict 
        for answer in st.session_state.answers:
            get_pattern[answer["name"]]={'pattern':answer["pattern"], 'descriptions':answer["description"], 'example':answer['example']}

        # Add the data in a DataFrame
        data = {'Language': [language], 'Tag': [tag],'value': [deprel],'overview':[overview], 'general_ex':[general_ex],'upos_and_value_feats':[upos_value] ,'specific_pattern':[get_pattern]}
        df = pd.DataFrame(data)

    if len(deprel) > 1:
        st.write("Choose only one tag!")

##################################################################################
######################## OTHER LING PHENOMENA ####################################
##################################################################################  

if tag == "Other linguistic phenomena":

    # dict to get the upos that can have the features? 
    upos_value = {}

    # name of the features
    ling = st.text_input(f"What is the linguistic phenomena ? ")

    if ling in particular_phenomena_check:
        st.write("You have to write your phenomena in the 'particular_phenomena' section because a page already exists\n Please change.")
    else:

        # short description of the features
        overview = st.text_area(f"Can you give a short description of the linguistic phenomena {ling} in your language ? ",height=200) 
        
        # give general example
        general_ex = st.text_area(f"Conll example",height=200)

    
        # THe user can add some pattern to describe in his page 
        add_pattern = st.radio("Can you describe more your pattern ? ",('Yes','No'))
        if add_pattern == "Yes":
            st.write("Describe your pattern")
            # fonction add_answer()
            add_answer()
        get_pattern = {}
        # we get the information from the function and put them in a dict 
        for answer in st.session_state.answers:
            get_pattern[answer["name"]]={'pattern':answer["pattern"], 'descriptions':answer["description"], 'example':answer['example']}

        # Add the data in a DataFrame
        data = {'Language': [language], 'Tag': [tag],'value': [ling],'overview':[overview], 'general_ex':[general_ex],'upos_and_value_feats':[dict()],'specific_pattern':[get_pattern]}
        df = pd.DataFrame(data)


##################################################################################
######################## ENREGISTREMENT DES DONNE ################################
################ ET ECRITURE DANS LE GUIDE D'ANNOTATION ##########################
##################################################################################
# Reset the form
if st.button("Delete"):
    st.session_state.answers = []

# Save the data in JSON file
if st.button('Enregistrer au format JSON'):
    if tag == 'Syntactic_relations' or tag == 'Features' or tag =='Misc' or tag=='Upos' or tag =="Deep":
        named = data['value'][0]
    # on ajoute des underscore pour la page du phenomen linguistic pour le nom du fichier. 
    if tag == 'Other linguistic phenomena':
        named = str(data['value'][0])
        named = named.split(" ")
        named = "_".join(named)
    if tag =='Universal_construction':
        named = " ".join(data["value"][0])

    df.to_json(f'{str(language).lower()}/output/output_{str(language).lower()}_{named}.json', orient='records')
    st.write(f"The request file {str(language).lower()}/output/output_{str(language).lower()}_{named}.json has been saved.")
    st.title("Saving your answer and updating the guidelines, dont quit :warning:")
    st.markdown(":warning: :red[Don't quit the formulare while you're not welcome to] :warning:")
    # Exécution conditionnelle du code après l'enregistrement du fichier -> on rédige les fichiers et on les place au bon endroit. Ici on considère
    # que l'utilisateur a écrit des patterns pour créer une table 
    if f'{str(language).lower()}/output/output_{str(language).lower()}_{named}.json' and data['specific_pattern'] != [{}]:
        st.markdown("## Writing the table link to grew-match")
        st.write("Writing of the request file for the table...")
        # # Ecriture du fichier request pour construire les tables dans le sous dossier langue/langue_request_json/...

        # contenu pour les requête
        content = create_request_file(f"{str(language).lower()}/output/output_{str(language).lower()}_{named}.json")

        with open(f"{str(language).lower()}/{str(language).lower()}_request_json/request_output_{str(language).lower()}_{named}.json",'w') as f:
            f.write(str(content))
        st.write(f" The request file has been saved : {str(language).lower()}/{str(language).lower()}_request_json/request_output_{str(language).lower()}_{named}.json ")
        
        # Ecriture du fichier json pour les tables dans le sous dossier langue/langue_table_json/...
        st.write(f"Creation of the tables ag-grid in the sub-folder {language}/{language}_table_json/ ...")
        result = process_files(f"{str(language).lower()}/{str(language).lower()}_request_json/request_output_{str(language).lower()}_{named}.json", f"{str(language).lower()}/{str(language).lower()}_table_json/sud_{str(language).lower()}.json")
        with open(f"{str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{named}.json" ,'w') as f:
            f.write(str(result))
        st.write(f"The file : {str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{named}.json has been saved")
        
        # Ecriture du fichier markdown pour les pages dans le sous dossier langue/langue_page/...
        # CHANGEMENT : on écrit directement au bon endroit ! -> voir plus loin ! 
        #st.write("Ecriture de la page en markdown pour le guide d'annotation")
        md_output = json_to_markdown_fwith_pattern(f"{str(language).lower()}/output/output_{str(language).lower()}_{named}.json", f"{str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{named}.json")
        #md_output = add_link("links.csv",md_output)
        with open(f"{str(language).lower()}/{str(language).lower()}_page/output_{str(language).lower()}_{named}.md",'w') as f:
            f.write(md_output)
        #st.write(f"Le fichier MarkDown est écrit : output_{str(language).lower()}_{named}.md\n")

        st.write("We move the table to the right place...")
        # On déplace le fichier des tables au bon endroit dans la partie static si l'utilisateur a écrit une page relative à un TAG
        if tag == 'Features' or tag =='Misc' or tag=='Upos' or tag =="Deep" or tag =="Universal_construction":
            old_path = f"{str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{named}.json"
            new_path = f"../static/docs/general_guideline/{tag}/{named}/table_output_{str(language).lower()}_{named}.json"
            os.rename(old_path,new_path)
        
        # traitement différent si deprel
        if tag == "Syntactic_relations":
            old_path = f"{str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{named}.json"
            
            if named == "subj" or named =="mod" or named =="compound" or named =="udep" or named=="flat" or named.startswith("comp") or named.startswith("conj"):
                new_path = f"../static/docs/general_guideline/{tag}/{named}/{named}/table_output_{str(language).lower()}_{named}.json"
            
            if named == "discourse" or named == "dislocated" or named =="vocative" or named.startswith("parataxis"):
                new_path = f"../static/docs/general_guideline/{tag}/macrosyntaxe/{named}/table_output_{str(language).lower()}_{named}.json"
            
            # on bouge les fichiers table.json
            os.rename(old_path,new_path)
        
        st.write("Table has been moved.")

        st.markdown("## Writting the guideline's page")
        st.write("guideline's page writting...")
        # On ajoute le texte au bon endroit si l'utilisateur a écrit une page relative à un TAG
        if tag == 'Features' or tag =='Misc' or tag=='Upos' or tag =="Deep" or tag=="Universal_construction":
            if f"../content/docs/general_guideline/{tag}/{named}.md":
                add_text(f"../content/docs/general_guideline/{tag}/{named}.md", f"\n\n{md_output} \n\n", f"## {str(language).lower()}\n")

        # On traitement différent les relarions syntaxiques car organisé autrement dans le guide
        if tag == "Syntactic_relations":
            if named == "subj" or named =="mod" or named =="compound" or named =="udep" or named=="flat" or named.startswith("comp") or named.startswith("conj"):
                if f"../content/docs/general_guideline/{tag}/{named}/{named}.md":
                    add_text(f"../content/docs/general_guideline/{tag}/{named}/{named}.md", f"\n\n{md_output} \n\n", f"## {str(language).lower()}\n")
            
            if named == "discourse" or named == "dislocated" or named =="vocative" or named.startswith("parataxis"):
                if f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/{named}.md":
                    add_text(f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/{named}.md", f"\n\n{md_output} \n\n", f"## {str(language).lower()}\n")
        st.write("guideline's page has been written.")

        
        # Sinon on crée une page pour un phénomène linguistique, on ajoute une nouvelle page au bon endroit
        if tag == "Other linguistic phenomena":
            name = str(data['value'][0])
            name = name.split(" ")
            name = "_".join(name)
            st.markdown(f"## Creating the guideline's page \n ../content/docs/language/{str(language).lower()}/{name}.md ...")
            os.mkdir(f"../static/docs/language/{str(language).lower()}/{name}")
            with open(f"../content/docs/language/{str(language).lower()}/{name}.md", 'w') as f:
                f.write(md_output)
            st.markdown(f"Guideline's page has been creating.")
            st.write("Mooving the table in the right place...")
            # Et on bouge la table à l'endroit correspondant dans la partie static (TODO : vérifier que ça fonctionne bien)
            old_path = f"{str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{name}.json"
            new_path = f"../static/docs/language/{str(language).lower()}/{name}/table_output_{str(language).lower()}_{name}.json"
            os.rename(old_path,new_path)
            st.write("The table has been moved.")
    st.write("You can quit the formular !")


    # S'il n'y pas de pattern specific pour construire les tables, on enlève une étape et on utilise une autre fonction de json2md.py

    if f'{str(language).lower()}/output/output_{str(language).lower()}_{named}.json' and data['specific_pattern'] == [{}]:

        st.write("Ecriture du fichier markdown dans le sous dossier langue/langue_page/")
        # Ecriture du fichier markdown pour les pages dans le sous dossier langue/langue_page/...
        md_output = json_to_markdown_no_pattern(f"{str(language).lower()}/output/output_{str(language).lower()}_{named}.json")
        #md_output = add_link("links.csv",md_output)
        with open(f"{str(language).lower()}/{str(language).lower()}_page/output_{str(language).lower()}_{named}.md",'w') as f:
            f.write(md_output)
        
        st.write("On ajoute la page markdown au bon endroit dans le guide d'annotation")
        # On ajoute le texte au bon endroit si l'utilisateur a écrit une page relative à un TAG
        if tag == 'Features' or tag =='Misc' or tag=='Upos' or tag =="Deep" or tag=="Universal_construction":
            if f"../content/docs/general_guideline/{tag}/{named}.md":
                add_text(f"../content/docs/general_guideline/{tag}/{named}.md", f"\n\n{md_output} \n\n", f"## {str(language).lower()}\n")

        # On traitement différent les relarions syntaxiques car organisé autrement dans le guide
        if tag == "Syntactic_relations":
            if named == "subj" or named =="mod" or named =="compound" or named =="udep" or named=="flat" or named.startswith("comp") or named.startswith("conj"):
                if f"../content/docs/general_guideline/{tag}/{named}/{named}.md":
                    add_text(f"../content/docs/general_guideline/{tag}/{named}/{named}.md", f"\n\n{md_output} \n\n", f"## {str(language).lower()}\n")
            
            if named == "discourse" or named == "dislocated" or named =="vocative" or named.startswith("parataxis"):
                if f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/{named}.md":
                    add_text(f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/{named}.md", f"\n\n{md_output} \n\n", f"## {str(language).lower()}\n")

        # Sinon on crée une page typique, on ajoute une nouvelle page au bon endroit
        if tag == "Other linguistic phenomena":
            name = str(data['value'][0])
            name = name.split(" ")
            name = "_".join(name)
            st.write(f"../content/docs/language/{str(language).lower()}/{name}.md")
            with open(f"../content/docs/language/{str(language).lower()}/{name}.md", 'w') as f:
                f.write(md_output)

        st.write("Vous pouvez quitter le formulaire")
    

    get_percent_to_write = parcourir_arborescence("../content/docs/general_guideline", f"{str(language).lower()}")
    print(get_percent_to_write)
    add_text_check(f"../content/docs/language/{str(language).lower()}/_index.md", f"Statut of the guideline : {get_percent_to_write}% written\n", f"### Guidelines status\n")
