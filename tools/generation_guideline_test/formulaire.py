import streamlit as st
import pandas as pd
from create_request_from_json import create_request_file
from json2md import json_to_markdown_feats_misc, add_link
from test_build_table import process_files

"""
 streamlit run formulaire.py
"""

liste_of_upos = ['AUX','ADV','DET','VERB','SYM','X','CCONJ','SCONJ','ADJ','PRON','PROPN','INTJ','ADP','NUM','PART','PUNCT']

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
    if st.button('Add'):
        answers.append({'name':name,'description': descr, 'pattern': pattern, 'example':example})
    
    # update the list of answers during the session. 
    st.session_state.answers = answers


# Formular 

# Get the language
language = st.text_input('Name of the language')

# Get the type of page that the user want to write. 
tag = st.radio("What do you want to documentate ? ", ('DEPREL','FEATS','MISC','Upos','Other linguistic phenomena'))

# Different type of page
if tag == 'FEATS' or tag =="MISC":
    """
    Text zone to write the a Feature's page for the guideline. 
    """

    # dict to get the upos that can have the features? 
    upos_value = {}

    # name of the features
    feats = st.text_input(f"What is the {tag} ? ")

    # short description of the features
    overview = st.text_area(f"Can you give a short description of the feature {feats} in your language ? ", height=200) 
    
    # which upos can have the features 
    which_upos = st.multiselect(f'which upos are conserned by the feature {feats} ?', liste_of_upos)

    # for each upos, we can indicates the feature's value 
    for i in range(len(which_upos)):
        combo_value_feats = st.text_input(f"Which are the value of the features {feats} for the upos {which_upos[i]} ? (put a ';' between each value)")
        combos = combo_value_feats.split(";")
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
    data = {'Language': [language], 'Tag': [tag],'value': [feats],'overview':[overview],'upos_and_value_feats':[upos_value] ,'specific_pattern':[get_pattern]}
    df = pd.DataFrame(data)


###############


# Different type of page
if tag == 'Upos':
    """
    Text zone to write the a Feature's page for the guideline. 
    """

    # dict to get the feats that can be on the upos
    features_name = {}

    # name of the features
    upos = st.text_input(f"What is the {tag} ? ")

    # short description of the features
    overview = st.text_area(f"Can you give a short description of the feature {upos} in your language ? ", height=200) 

    # which upos can have the features 
    which_features = st.text_area(f"Which features can be on the {upos} ? (put a ';' between each value)",height=200)

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
    data = {'Language': [language], 'Tag': [tag],'value': [upos],'overview':[overview],'upos_and_value_feats':[features_name] ,'specific_pattern':[get_pattern]}
    df = pd.DataFrame(data)

############

# Different type of page
if tag == 'DEPREL':
    """
    Text zone to write the a Feature's page for the guideline. 
    """
    # dict to get the upos that can have the features? 
    upos_value = {}

    # name of the features
    deprel = st.text_input(f"What is the {tag} ? ")

    # short description of the features
    overview = st.text_area(f"Can you give a short description of the feature {deprel} in your language ? ",height=200) 
    
    # which upos can have the features 
    which_upos = st.multiselect(f'which upos can be the head of the {deprel} ?', liste_of_upos)

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
    data = {'Language': [language], 'Tag': [tag],'value': [deprel],'overview':[overview],'upos_and_value_feats':[upos_value] ,'specific_pattern':[get_pattern]}
    df = pd.DataFrame(data)

if tag == "Other linguistic phenomena":
    """
    Text zone to write the a Feature's page for the guideline. 
    """

    # dict to get the upos that can have the features? 
    upos_value = {}

    # name of the features
    ling = st.text_input(f"What is the {tag} ? ")

    # short description of the features
    overview = st.text_area(f"Can you give a short description of the linguistic phenomena {ling} in your language ? ",height=200) 
    
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
    data = {'Language': [language], 'Tag': [tag],'value': [ling],'overview':[overview],'upos_and_value_feats':[upos_value] ,'specific_pattern':[get_pattern]}
    df = pd.DataFrame(data)

# Save the data in JSON file
if st.button('Enregistrer au format JSON'):
    df.to_json(f'output_{language}_{data["value"][0]}.json', orient='records')
    #st.write('Les données ont été enregistrées au format JSON.')
    # Exécution conditionnelle du code après l'enregistrement du fichier
    if f'output_{language}_{data["value"][0]}.json':
        st.write(f"Le fichier output_{language}_{data['value'][0]}.json a été enregistré.")
        content = create_request_file(f"output_{language}_{data['value'][0]}.json")
        with open(f"request_output_{language}_{data['value'][0]}.json",'w') as f:
            f.write(str(content))
        result = process_files(f"request_output_{language}_{data['value'][0]}.json", f"../{str(language).lower()}_table_json/sud_{language}.json")
        with open(f"table_output_{language}_{data['value'][0]}.json" ,'w') as f:
            f.write(str(result))
        md_output = json_to_markdown_feats_misc(f"output_{language}_{data['value'][0]}.json")
        md_output = add_link("links.csv",md_output)
        with open(f"output_{language}_{data['value'][0]}.md") as f:
            f.write(md_output)