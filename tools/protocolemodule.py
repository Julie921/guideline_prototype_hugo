"""
Ce fichier .py contient les fonctions utilisées pour les protocoles de vérifications. 
"""

def compare_three_listes(liste1, liste2, liste3):
    difference = []
    for element in liste1:
        if element not in liste2 and element not in liste3:
            difference.append(element)
    for element in liste2:
        if element not in liste1 and element not in liste3:
            difference.append(element)
    for element in liste3:
        if element not in liste1 and element not in liste2:
            difference.append(element)
    return difference

def compare_two_listes(liste1, liste2):
    difference = []
    for element in liste1:
        if element not in liste2:
            difference.append(element)
    for element in liste2:
        if element not in liste1:
            difference.append(element)
    return difference
