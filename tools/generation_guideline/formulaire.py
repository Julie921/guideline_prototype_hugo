import streamlit as st
import pandas as pd

"""
Il n'y a que pour la valeur FEATS que j'ai rédigé le formulaire
"""

def add_answer():
    answers = st.session_state.get('answers', [])
    name = st.text_input("Name")
    pattern = st.text_input('Pattern')
    descr = st.text_input('Description')
    example = st.text_input('Example (conll)')
    if st.button('Ajouter'):
        answers.append({'name':name,'description': descr, 'pattern': pattern, 'example':example})
    st.session_state.answers = answers


language = st.text_input('Name of the language')
tag = st.radio("What do you want to documentate ? ", ('DEPREL','FEATS','MISC','Upos','Other linguistic phenomena'))

if tag == 'FEATS':
    upos_value = {}
    feats = st.text_input(f"What is the {tag} ? ")
    overview = st.text_input(f"Can you give a short description of the feature {feats} in your language ? ") 
    which_upos = st.multiselect(f'which upos are conserned by the feature {feats} ?', ['AUX', 'ADV'])
    st.write(type(which_upos))
    for i in range(len(which_upos)):
        combo_value_feats = st.text_input(f"Which are the value of the features {feats} for the upos {which_upos[i]} ? (put a ';' between each value)")
        combos = combo_value_feats.split(";")
        upos_value[which_upos[i]] = combos
    add_pattern = st.radio("Du you want to describe some specifs patterns ? ",('Yes','No'))
    if add_pattern == "Yes":
        st.write("Describe your pattern")
        add_answer()
    get_pattern = {}
    for answer in st.session_state.answers:
        get_pattern[answer["name"]]={'pattern':answer["pattern"], 'descriptions':answer["description"], 'example':answer['example']}
    st.write(get_pattern)
    # Ajout des données saisies dans un dataframe Pandas
    data = {'Language': [language], 'Tag': [tag],'value': [feats],'overview':[overview],'upos_and_value_feats':[upos_value] ,'specific_pattern':[get_pattern]}
    df = pd.DataFrame(data)

# Enregistrement des données saisies au format JSON
if st.button('Enregistrer au format JSON'):
    df.to_json('output.json', orient='records')
    st.write('Les données ont été enregistrées au format JSON.')




