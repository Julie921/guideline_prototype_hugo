import streamlit as st
import pandas as pd
from create_request_from_json import create_request_file
from json2md import json_to_markdown_feats_misc, add_link,json_to_markdown_no_pattern
from test_build_table import process_files
import os 

"""
streamlit run formulaire.py
"""

liste_of_upos = ['AUX','ADV','DET','VERB','SYM','X','CCONJ','SCONJ','ADJ','PRON','PROPN','INTJ','ADP','NUM','PART','PUNCT','NOUN']

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


# Formular 

# Get the language
language = st.text_input('Name of the language')

# Get the type of page that the user want to write. 
tag = st.radio("What do you want to documentate ? ", ('Syntactic_relations','Features','MISC','Upos','Other linguistic phenomena','Deep'))

# Different type of page
if tag == 'Features' or tag =="MISC":
    """
    Text zone to write the a Feature's or MISC's page for the guideline. 
    """

    # dict to get the upos that can have the features? 
    upos_value = {}

    # name of the features
    feats = st.text_input(f"What is the {tag} ? ")

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


###############


# Different type of page
if tag == 'Upos':
    """
    Text zone to write the upos page for the guideline. 
    """

    # dict to get the feats that can be on the upos
    features_name = {}

    # name of the features
    upos = st.text_input(f"What is the {tag} ? ")

    # short description of the features
    overview = st.text_area(f"Can you give a short description of the feature {upos} in your language ? ", height=200) 

    # give general example
    general_ex = st.text_area(f"Conll example",height=200)

    # which upos can have the features 
    which_features = st.text_area(f"Which features can be on the {upos} ? (put a ';' between each value) (optional)",height=200)

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

############

# Different type of page
if tag == 'Syntactic_relations' or tag == 'Deep':
    """
    Text zone to write the a syntactic relation's page for the guideline. 
    """
    # dict to get the upos that can have the features? 
    upos_value = {}

    # name of the features
    deprel = st.text_input(f"What is the {tag} ? ")

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

if tag == "Other linguistic phenomena":

    # dict to get the upos that can have the features? 
    upos_value = {}

    # name of the features
    ling = st.text_input(f"What is the linguistic phenomena ? ")

    # short description of the features
    overview = st.text_area(f"Can you give a short description of the linguistic phenomena {ling} in your language ? ",height=200) 
    
    # give general example
    general_ex = st.text_area(f"Conll example",height=200)
    
    # # which upos can have the features 
    # which_upos = st.multiselect(f'which features, upos or deprel are conserned by the phenomena ?', liste_of_upos)

    # # for each upos, we can indicates the feature's value 
    # for i in range(len(which_upos)):
    #     combo_value_feats = st.text_input(f"Which are the value of the features {feats} for the upos {which_upos[i]} ? (put a ';' between each value)")
    #     combos = combo_value_feats.split(";")
    #     upos_value[which_upos[i]] = combos
    
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
    data = {'Language': [language], 'Tag': [tag],'value': [ling],'overview':[overview], 'general_ex':[general_ex], 'upos_and_value_feats':[upos_value] ,'specific_pattern':[get_pattern]}
    df = pd.DataFrame(data)

st.write(f"specific pattern : {data['specific_pattern']}")

# Save the data in JSON file
if st.button('Enregistrer au format JSON'):
    if tag == 'Syntactic_relations' or tag == 'Features' or tag =='MISC' or tag=='Upos' or tag =="Deep":
        named = data['value'][0]
    if tag == 'Other linguistic phenomena':
        named = str(data['value'][0])
        named = named.split(" ")
        named = "_".join(named)

    df.to_json(f'{str(language).lower()}/output/output_{str(language).lower()}_{named}.json', orient='records')
    #st.write('Les données ont été enregistrées au format JSON.')

    # Exécution conditionnelle du code après l'enregistrement du fichier -> on rédige les fichiers et on les place au bon endroit
    if f'{str(language).lower()}/output/output_{str(language).lower()}_{named}.json' and data['specific_pattern'] != [{}]:

        # Ecriture du fichier request pour construire les tables dans le sous dossier langue/langue_rrequest_json/...
        st.write(f"Le fichier {str(language).lower()}/output/output_{str(language).lower()}_{named}.json a été enregistré.")
        content = create_request_file(f"{str(language).lower()}/output/output_{str(language).lower()}_{named}.json")
        with open(f"{str(language).lower()}/{str(language).lower()}_request_json/request_output_{str(language).lower()}_{named}.json",'w') as f:
            f.write(str(content))
        st.write(f"Le fichier de requête pour construire les tables est fait : {str(language).lower()}/{str(language).lower()}_request_json/request_output_{str(language).lower()}_{named}.json ")
        
        # Ecriture du fichier json pour les tables dans le sous dossier langue/langue_table_json/...
        result = process_files(f"{str(language).lower()}/{str(language).lower()}_request_json/request_output_{str(language).lower()}_{named}.json", f"{str(language).lower()}/{str(language).lower()}_table_json/sud_{str(language).lower()}.json")
        with open(f"{str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{named}.json" ,'w') as f:
            f.write(str(result))
        st.write(f"Le fichier contenant les tables ag-grid est fait : {str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{named}.json ")
        
        # Ecriture du fichier markdown pour les pages dans le sous dossier langue/langue_page/...
        md_output = json_to_markdown_feats_misc(f"{str(language).lower()}/output/output_{str(language).lower()}_{named}.json", f"{str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{named}.json")
        md_output = add_link("links.csv",md_output)
        with open(f"{str(language).lower()}/{str(language).lower()}_page/output_{str(language).lower()}_{named}.md",'w') as f:
            f.write(md_output)
        st.write(f"Le fichier MarkDown est écrit : output_{str(language).lower()}_{named}.md\n\n Vous pouvez quitter le formulaire.")

        # On déplace le fichier des tables au bon endroit dans la partie static si l'utilisateur a écrit une page relative à un TAG
        if tag == 'Syntactic_relations' or tag == 'Features' or tag =='MISC' or tag=='Upos' or tag =="Deep":
            old_path = f"{str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{named}.json"
            new_path = f"../static/docs/general_guideline/{tag}/{named}/table_output_{str(language).lower()}_{named}.json"
            os.rename(old_path,new_path)
        
        # On ajoute le texte au bon endroit si l'utilisateur a écrit une page relative à un TAG
        if tag == 'Features' or tag =='MISC' or tag=='Upos' or tag =="Deep":
            if f"../content/docs/general_guideline/{tag}/{named}.md":
                with open(f"../content/docs/general_guideline/{tag}/{named}.md", 'a') as f:
                    f.write("\n\n"+md_output+"\n\n")
        
        if tag == "Syntactic_relations":
            if named == "subj" or named =="mod" or named =="compound" or named =="udep" or named=="flat":
                if f"../content/docs/general_guideline/{tag}/{named}/{named}.md":
                    with open(f"../content/docs/general_guideline/{tag}/{named}/{named}.md",'a') as f:
                        f.write("\n\n"+md_output+"\n\n")
            
            if named.startswith("comp"):
                if named == "comp":
                    if f"../content/docs/general_guideline/{tag}/comp/_index.md":
                        with open(f"../content/docs/general_guideline/{tag}/conj/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")
                else:
                    if f"../content/docs/general_guideline/{tag}/comp/{named}.md":
                        with open(f"../content/docs/general_guideline/{tag}/comp/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")

            if named.startswith("conj"):
                if named == "conj":
                    if f"../content/docs/general_guideline/{tag}/conj/_index.md":
                        with open(f"../content/docs/general_guideline/{tag}/conj/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")
                else:
                    if f"../content/docs/general_guideline/{tag}/conj/{named}.md":
                        with open(f"../content/docs/general_guideline/{tag}/conj/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")
            
            if named == "discourse" or named == "dislocated" or named =="vocative":
                if f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/{named}.md":
                    with open(f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/{named}.md",'a') as f:
                        f.write("\n\n"+md_output+"\n\n")

            if named.startswith("parataxis"):
                if named == "parataxis":
                    if f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/_index.md":
                        with open(f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/_index.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n") 
                else:
                    if f"../content/docs/general_guideline/{tag}/macrosyntaxe/parataxis/{named}.md":
                        with open(f"../content/docs/general_guideline/{tag}/macrosyntaxe/parataxis/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")

        
        # Sinon on crée une page typique, on ajoute une nouvelle page au bon endroit
        if tag == "Other linguistic phenomena":
            name = str(data['value'][0])
            name = name.split(" ")
            name = "_".join(name)
            with open(f"../content/docs/general_guideline/language/{str(language).lower()}/{name}.md", 'w') as f:
                f.write(md_output)
            # Et on bouge la table à l'endroit correspondant dans la partie static (TODO : vérifier que ça fonctionne bien)
            old_path = f"{str(language).lower()}/{str(language).lower()}_table_json/table_output_{str(language).lower()}_{name}.json"
            new_path = f"../static/docs/language/{str(language).lower()}/{data['value'][0]}/table_output_{str(language).lower()}_{name}.json"
            os.rename(old_path,new_path)

    # S'il n'y pas de pattern specific pour construire les tables 

    if f'{str(language).lower()}/output/output_{str(language).lower()}_{named}.json' and data['specific_pattern'] == [{}]:
        # Ecriture du fichier markdown pour les pages dans le sous dossier langue/langue_page/...
        md_output = json_to_markdown_no_pattern(f"{str(language).lower()}/output/output_{str(language).lower()}_{named}.json")
        md_output = add_link("links.csv",md_output)
        with open(f"{str(language).lower()}/{str(language).lower()}_page/output_{str(language).lower()}_{named}.md",'w') as f:
            f.write(md_output)
        #st.write(f"Le fichier MarkDown est écrit : output_{str(language).lower()}_{named}.md\n\n Vous pouvez quitter le formulaire.")
        
        # On ajoute le texte au bon endroit si l'utilisateur a écrit une page relative à un TAG
        if tag == 'Features' or tag =='MISC' or tag=='Upos' or tag =="Deep":
            if f"../content/docs/general_guideline/{tag}/{named}.md":
                with open(f"../content/docs/general_guideline/{tag}/{named}.md", 'a') as f:
                    f.write("\n\n"+md_output+"\n\n")
        
        if tag == "Syntactic_relations":
            if named == "subj" or named =="mod" or named =="compound" or named =="udep" or named=="flat":
                if f"../content/docs/general_guideline/{tag}/{named}/{named}.md":
                    with open(f"../content/docs/general_guideline/{tag}/{named}/{named}.md",'a') as f:
                        f.write("\n\n"+md_output+"\n\n")
            
            if named.startswith("comp"):
                if named == "comp":
                    if f"../content/docs/general_guideline/{tag}/comp/_index.md":
                        with open(f"../content/docs/general_guideline/{tag}/conj/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")
                else:
                    if f"../content/docs/general_guideline/{tag}/comp/{named}.md":
                        with open(f"../content/docs/general_guideline/{tag}/comp/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")

            if named.startswith("conj"):
                if named == "conj":
                    if f"../content/docs/general_guideline/{tag}/conj/_index.md":
                        with open(f"../content/docs/general_guideline/{tag}/conj/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")
                else:
                    if f"../content/docs/general_guideline/{tag}/conj/{named}.md":
                        with open(f"../content/docs/general_guideline/{tag}/conj/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")
            
            if named == "discourse" or named == "dislocated" or named =="vocative":
                if f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/{named}.md":
                    with open(f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/{named}.md",'a') as f:
                        f.write("\n\n"+md_output+"\n\n")

            if named.startswith("parataxis"):
                if named == "parataxis":
                    if f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/_index.md":
                        with open(f"../content/docs/general_guideline/{tag}/macrosyntaxe/{named}/_index.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n") 
                else:
                    if f"../content/docs/general_guideline/{tag}/macrosyntaxe/parataxis/{named}.md":
                        with open(f"../content/docs/general_guideline/{tag}/macrosyntaxe/parataxis/{named}.md",'a') as f:
                            f.write("\n\n"+md_output+"\n\n")
        
        # Sinon on crée une page typique, on ajoute une nouvelle page au bon endroit
        if tag == "Other linguistic phenomena":
            name = str(data['value'][0])
            name = name.split(" ")
            name = "_".join(name)
            with open(f"../content/docs/general_guideline/language/{str(language).lower()}/{name}.md", 'w') as f:
                f.write(md_output)