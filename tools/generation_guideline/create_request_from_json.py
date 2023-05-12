"""
Script pour créer un validateur via une page de règle générer depuis le formulaire.
"""

import json 
import argparse

"""
On commence par créer le dictionnaire avec la structure général 
title = titre de la page
langugae = code du langage (à ajouter au formilaire)
item = chaque pattern avec leur description associé 
"""

def create_request_file(data):
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
    with open("request_output.json","w") as output:
        content = str(liste_dict_pattern)
        content = content.replace("'",'"')
        output.write(str(content))



if __name__ == '__main__':
    # Configuration des arguments de ligne de commande
    parser = argparse.ArgumentParser(description='Create the request file in JSON format')
    parser.add_argument('file_json', metavar='file_json', type=str, help="path to the formular JSON File")
    
    # Parsing des arguments en ligne de commande
    args = parser.parse_args()

    # Lecture du fichier JSON passé en argument en ligne de commande
    with open(args.file_json, "r") as json_file: 
        data = json.load(json_file)

    # Lancer la lecture pour écrire le fichier request au format JSON
    create_request_file(data)






    