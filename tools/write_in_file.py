"""
Module pour ajouter le texte markdown au bon endroit. 
"""

def add_text(fichier, texte_a_ajouter, texte_repere):
    # Lire le contenu existant du fichier
    with open(fichier, 'r') as f:
        contenu = f.readlines()

    print(contenu)
    get_index_lang = contenu.index("## French \n")
    print(get_index_lang)
    contenu.pop(get_index_lang+2)

    print(contenu)

    # Rechercher le texte de repère dans le contenu
    try:
        index = contenu.index(texte_repere)
    except ValueError:
        print("Le texte de repère n'a pas été trouvé dans le fichier.")
        with open(fichier, 'a') as f:
            f.writelines(contenu)
        return

    # Insérer le texte à ajouter après le texte de repère
    contenu.insert(index + 1, texte_a_ajouter)

    # Écrire le contenu modifié dans le fichier
    with open(fichier, 'w') as f:
        f.writelines(contenu)


if __name__ == '__main__':
    # Exemple d'utilisation
    fichier = 'random_files.md'
    texte_a_ajouter = 'Texte à ajouter'
    position_dans_le_fichier = "## French \n"

    add_text(fichier, texte_a_ajouter, position_dans_le_fichier)