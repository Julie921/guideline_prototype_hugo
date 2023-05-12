"""
Script pour créer un validateur via une page de règle générer depuis le formulaire.
"""

import json 

"""
On commence par créer le dictionnaire avec la structure général 
title = titre de la page
langugae = code du langage (à ajouter au formilaire)
item = chaque pattern avec leur description associé 
"""


with open("output.json", "r") as json_file: 
    data = json.load(json_file)



liste_dict_pattern = []

for key,value in data.items():
    if key == "specific_pattern":
        for keyz,valuez in value.items():
            dict_pattern = {}
            id = keyz.split(" ")
            dict_pattern["id"]="_".join(id)
            for kk,vv in valuez.items():
                if kk == "pattern":
                    dict_pattern["request"]=[{"pattern":[vv]}]
            liste_dict_pattern.append(dict_pattern)

print(liste_dict_pattern)

with open("tables_output.json","w") as output:
    content = str(liste_dict_pattern)
    content = content.replace("'",'"')
    output.write(str(content))



    