import sys 
from pathlib import Path
import os 
import re

dossier_racine = Path(sys.argv[1])

import os


import os

# Chemin du dossier racine à explorer

# Liste pour enregistrer les liens des fichiers
liens_fichiers = []

# Parcours de l'arborescence de dossiers de manière récursive
for dossier, sous_dossiers, fichiers in os.walk(dossier_racine):
    for fichier in fichiers:
        # Création du chemin absolu vers le fichier
        chemin_fichier = os.path.join(dossier, fichier)
        # Ajout du chemin du fichier à la liste
        liens_fichiers.append(chemin_fichier)

# expression régulière pour récupérer toutes les pages d'instructions d'annotations de la partie générale du guide !
links_re = re.compile(r".*/content/(docs/general_guideline/.*)")
tag = re.compile(r".*/content/docs/general_guideline/(.*/)+(\w+).md")

dict_link = {}
# # Affichage des liens des fichiers enregistrés dans la liste
for element in liens_fichiers:
		# on match l'expression régulière d'un dossier avec les noms de dossiers
		m = re.match(links_re,element)
		if m:
			# si on est dans un dossier, on cherche le tag (.md) pour récupérer le tag associé au bon chemin
			n = re.match(tag,element)
			if n:
				# on ajoute les information dans le dictionnaire dict_link[chemin relatif]=tag
				dict_link[m.group(1)]=n.group(2)


#print(dict_link)

# on écrit les résultats dans un fichier .csv
with open("links.csv","w",encoding="utf-8") as output:
	output.write("tag;link")
	for key,value in dict_link.items():
		output.write(f"{str(value)};{str(key)}\n") 
