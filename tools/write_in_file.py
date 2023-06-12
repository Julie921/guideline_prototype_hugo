"""
Module pour ajouter le texte markdown au bon endroit. 
"""

import os
from typing import List

def add_text(fichier, texte_a_ajouter, texte_repere):
    new_contenu = []
    # Lire le contenu existant du fichier
    with open(fichier, 'r') as f:
        contenu = f.readlines()


    # Rechercher le texte de repère dans le contenu
    try:
        index = contenu.index(texte_repere)
    except ValueError:
        print("Le texte de repère n'a pas été trouvé dans le fichier.")
        # with open(fichier, 'w') as f:
        #     f.writelines(contenu)
        return

    # on récupère l'index du repère 
    ## crée nouvelle liste !!! + bsimple sinon impossible  
    get_index_lang = contenu.index(texte_repere)
    

    for i in range(get_index_lang):
        new_contenu.append(contenu[i])


    new_text = texte_a_ajouter.split("\n")

    # for element in new_text:
    #     print(f"element :{element}" )

    for element in new_text:
        new_contenu.append(f"{element}\n")
        #print(f"element :{element}" )

    if new_text[0] != texte_repere:
        new_text.pop(0)

    
    for i in range(get_index_lang+7,len(contenu)):
        new_contenu.append(contenu[i])

    #print(new_contenu)           
    #Écrire le contenu modifié dans le fichier
    with open(fichier, 'w') as f:
        f.writelines(new_contenu)

def add_text_check(fichier, texte_a_ajouter, texte_repere):
    # Lire le contenu existant du fichier
    with open(fichier, 'r') as f:
        contenu = f.readlines()

    print(contenu)
    # on récupère l'index du repère 
    get_index_lang = contenu.index(texte_repere)

    # on supprime le contenu que l'on veut changer
    contenu.pop(get_index_lang+2)

    # Rechercher le texte de repère dans le contenu
    try:
        index = contenu.index(texte_repere)
    except ValueError:
        print("Le texte de repère n'a pas été trouvé dans le fichier.")
        # with open(fichier, 'w') as f:
        #     f.writelines(contenu)
        return

    # Insérer le texte à ajouter après le texte de repère
    contenu.insert(index + 2, texte_a_ajouter)

    # Écrire le contenu modifié dans le fichier
    with open(fichier, 'w') as f:
        f.writelines(contenu)

def parcourir_arborescence(repertoire,langue):
    nombre_fichiers = 0  # Variable pour compter les fichiers
    nombre_todo = 0 # recup TODO information
    for dossier_racine, sous_repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            if fichier.startswith("_"):
                pass
            else:
                chemin_fichier = os.path.join(dossier_racine, fichier)
                #print(chemin_fichier)
                contenu_fichier = lire_contenu_fichier(chemin_fichier)
                print(contenu_fichier)
                nombre_fichiers = nombre_fichiers +1 # Incrémenter le compteur de fichiers
                index = contenu_fichier.index(f"## {langue}\n")
                if contenu_fichier[index+2] == "TODO\n":
                    nombre_todo = nombre_todo +1
                    #print(f"Le fichier '{fichier}' est à rédiger.")
    if nombre_fichiers == nombre_todo:
        if nombre_todo == 0:
            return 100
        else:
            return 0
    else:
        return round((1-nombre_todo/nombre_fichiers)*100,2)


def lire_contenu_fichier(chemin_fichier):
    with open(chemin_fichier, 'r') as file:
        contenu = file.readlines()
    return contenu


import os

def check_env(dossier_racine):
    v = True
    sous_dossiers = ['corpora', f'{dossier_racine}_page', f'{dossier_racine}_request_json', f'{dossier_racine}_table_json',"output"]

    if os.path.exists(dossier_racine):
        print(f"Le dossier racine '{dossier_racine}' existe.")
        
        for sous_dossier in sous_dossiers:
            chemin_sous_dossier = os.path.join(dossier_racine, sous_dossier)
            
            if os.path.exists(chemin_sous_dossier):
                continue
            else:
                v = False
    else:
        v = False
    
    return v


def read_partial_markdown(filename):
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        lines = contents.split("\n")
        output_lines = []
        subheading_count = 0
        exclude_code_block = False

        for line in lines:
            if line.startswith("{{<"):
                exclude_code_block = True
            elif line.startswith("{{</"):
                exclude_code_block = False
            elif not exclude_code_block:
                output_lines.append(line)

                if line.startswith("##"):
                    subheading_count += 1
                    if subheading_count == 2:
                        break

        output = "\n".join(output_lines)
        return output

if __name__ == '__main__':
    # Exemple d'utilisation
    fichier = '../content/docs/general_guideline/Upos/SYM.md'

    # with open("english/english_page/output_english_PRON.md","r") as f:
    #     texte_a_ajouter = ""
    #     line = f.readline()
    #     while line:
    #         texte_a_ajouter = texte_a_ajouter + line
    #         line = f.readline()

    position_dans_le_fichier = "## french\n"

    #add_text(fichier, texte_a_ajouter, position_dans_le_fichier)

    # Chemin du répertoire racine
    repertoire_racine = '../content/docs/general_guideline'

    # Appel de la fonction pour parcourir l'arborescence et compter les fichiers
    print(parcourir_arborescence(repertoire_racine,"french"))

    # Chemin du dossier racine à vérifier
    #dossier_racine = 'french'

    #Appel de la fonction pour vérifier l'arborescence
    #check_env(dossier_racine)