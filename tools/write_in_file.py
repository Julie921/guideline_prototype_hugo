"""
Module pour ajouter le texte markdown au bon endroit. 
"""

import os
from typing import List

def supp_text_univ_page(fichier:str, repere:str):
    pattern = [f"#{repere}","TODO\n","#### Overview\n","#### Specific Pattern\n"]
    new_content =""
    with open(fichier,'r', encoding="utf-8") as old:
        line = old.readline()
        while line:
            if line in pattern:
                pass
            else:
                new_content = new_content + line
            line = old.readline()

    with open(fichier,'w', encoding="utf-8") as new:
        new.write(new_content)


def add_text(fichier:str, texte_a_ajouter:str, texte_repere:str):
    """
    This function write a new content in a file, replaceb thanks to an identified text 'text_repere'
    Parameters
    ---------
    fichier : str
    texte_a_ajouter : str
    test_repere : str

    
    Return
    ---------
    None
    """
    # on crée une nouvelle liste pour récupérer le nouveau contenu
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
    get_index_lang = contenu.index(texte_repere)
    

    # ajouter le contenu dans la nouvelle liste, identique à l'ancien document jusqu'au texte repère
    for i in range(get_index_lang):
        new_contenu.append(contenu[i])


    # on met le texte à ajouter sous forme de liste
    new_text = texte_a_ajouter.split("\n")

    # for element in new_text:
    #     print(f"element :{element}" )

    # on ajoute le nouveau texte dans la nouvelle liste sauvegardant le nouveau document
    for element in new_text:
        new_contenu.append(f"{element}\n")

    # je sais plus
    if new_text[0] != texte_repere:
        new_text.pop(0)

    # et on ajoute le reste de l'ancien contenu
    for i in range(get_index_lang+7,len(contenu)):
        new_contenu.append(contenu[i])
         
    #Écrire le contenu modifié dans le fichier
    with open(fichier, 'w') as f:
        f.writelines(new_contenu)


def univ_add_text(fichier:str, texte_a_ajouter:str, texte_repere:str):
    """
    This function write a new content in a file, replaceb thanks to an identified text 'text_repere'
    Parameters
    ---------
    fichier : str
    texte_a_ajouter : str
    test_repere : str

    
    Return
    ---------
    None
    """
    # on crée une nouvelle liste pour récupérer le nouveau contenu
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
    get_index_lang = contenu.index(texte_repere)
    

    # ajouter le contenu dans la nouvelle liste, identique à l'ancien document jusqu'au texte repère
    for i in range(get_index_lang+1):
        new_contenu.append(contenu[i])


    # on met le texte à ajouter sous forme de liste
    new_text = texte_a_ajouter.split("\n")

    # for element in new_text:
    #     print(f"element :{element}" )

    # on ajoute le nouveau texte dans la nouvelle liste sauvegardant le nouveau document
    for element in new_text:
        new_contenu.append(f"{element}\n")

    #je sais plus
    if new_text[0] != texte_repere:
        new_text.pop(0)

    # et on ajoute le reste de l'ancien contenu
    for i in range(get_index_lang+1,len(contenu)):
        new_contenu.append(contenu[i])
         
    #Écrire le contenu modifié dans le fichier
    with open(fichier, 'w') as f:
        f.writelines(new_contenu)

    supp_text_univ_page(fichier,texte_repere)

def add_text_check(fichier, texte_a_ajouter, texte_repere):
    """
    This function write a new content in a file, replaced thanks to an identified text 'text_repere'. This function is used only to change the guideline's status
    Parameters
    ---------
    fichier : str
    texte_a_ajouter : str
    test_repere : str

    
    Return
    ---------
    None
    """
    # Lire le contenu existant du fichier
    with open(fichier, 'r') as f:
        contenu = f.readlines()

    #print(contenu)
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

def parcourir_arborescence(repertoire:str,langue:str)->int:
    """
    This function allows traversing a file/directory tree to count the number of properly filled pages for the general guidelines of a given language
    Parameters
    ---------
    repertoire : str
    langue : str

    Return
    ---------
    int
    """
    nombre_fichiers = 0  # Variable pour compter les fichiers
    nombre_todo = 0 # recup TODO information
    # parcourir arborescence 
    for dossier_racine, sous_repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            if fichier.startswith("_"):
                pass
            else:
                chemin_fichier = os.path.join(dossier_racine, fichier)
                # traitement différent selon si on se situe dans une construction universelle
                if chemin_fichier.startswith("../content/docs/general_guideline/Universal_construction"):
                    contenu_fichier = lire_contenu_fichier(chemin_fichier)
                    nombre_fichiers = nombre_fichiers +1
                    if f"### {langue}\n" in contenu_fichier:
                        index = contenu_fichier.index(f"### {langue}\n")
                        if contenu_fichier[index+2] == "TODO\n":
                            nombre_todo = nombre_todo+1
                    else:
                        pass    
                # ou dans une page relative à une étiquette
                else:
                    # on lit le contenu du fichier
                    contenu_fichier = lire_contenu_fichier(chemin_fichier)
                    # on compte le nb de fichier
                    nombre_fichiers = nombre_fichiers +1 # Incrémenter le compteur de fichiers
                    # on récupère l'endroit du fichier correspondant à la langue cible
                    if f"## {langue}\n" in contenu_fichier:
                        index = contenu_fichier.index(f"## {langue}\n")
                    # si le fichier n'est pas rempli, on incrémente la variable
                        if contenu_fichier[index+2] == "TODO\n":
                            nombre_todo = nombre_todo +1
                    else:
                        pass
                        #print(f"Le fichier '{fichier}' est à rédiger.")
    # on retourne l'information sous forme de %
    if nombre_fichiers == nombre_todo:
        if nombre_todo == 0:
            return 100
        else:
            return 0
    else:
        return round((1-nombre_todo/nombre_fichiers)*100,2)


def lire_contenu_fichier(chemin_fichier:str)->list:
    """
    This functions reads a file's content and return it in a list
    Parameters
    ---------
    repertoire : str
    langue : str

    Return
    ---------
    int
    """
    with open(chemin_fichier, 'r') as file:
        contenu = file.readlines()
    return contenu


import os

def check_env(dossier_racine:str)->bool:
    """
    This function check if the environement for a language is right 
    Parameters
    ---------
    repertoire : str (name of a language)


    Return
    ---------
    boolen
    """
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


def read_partial_markdown(filename:str)->str:
    """
    This function reads the starts of a markdown files (only the first second title), and return the content
    Parameters
    ---------
    filename : str

    Return
    ---------
    str
    """
    with open(filename, "r", encoding="utf-8") as file:
        # lecture du contenu du fichier
        contents = file.read()
        # contenu sous forme de liste (element = ligne)
        lines = contents.split("\n")
        # nouvelle liste pour output
        output_lines = []
        # variable pour compter sous titre
        subheading_count = 0
        # exclure les métadonnées
        exclude_metadata = False
        # exclure les balises pour les conlls
        exclude_code_block = False

        # on exclut les méta données
        for line in lines:
            if line.strip() == "---":
                exclude_metadata = not exclude_metadata
                continue
            
            if exclude_metadata:
                continue
            # on éclut les conlls
            if line.startswith("{{<"):
                exclude_code_block = True
                continue
            elif line.startswith("{{</"):
                exclude_code_block = False
                continue
            
            if exclude_code_block:
                continue
            
            # on ajoute seulement les lignes
            output_lines.append(line)

            # on s'arrête avant le début du deuxième titre (de niveau 2 ##)
            if line.startswith("##"):
                subheading_count += 1
                if subheading_count == 2:
                    break

        output = "\n".join(output_lines)
        # on retourn la variable sous forme de string
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
    repertoire_racine = '../content/docs/general_guideline/'

    # Appel de la fonction pour parcourir l'arborescence et compter les fichiers
    print(parcourir_arborescence(repertoire_racine,"french"))

    # Chemin du dossier racine à vérifier
    #dossier_racine = 'french'

    #Appel de la fonction pour vérifier l'arborescence
    #check_env(dossier_racine)

    supp_text_univ_page("../content/docs/general_guideline/Universal_construction/nominal_predicate_construction.md","french")