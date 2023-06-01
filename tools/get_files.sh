#!/bin/bash

# Chemin de la racine de l'arborescence
racine="../content/docs/general_guideline"

# Vérifier si le répertoire racine existe
if [ ! -d "$racine" ]; then
  echo "Le répertoire racine $racine n'existe pas."
  exit 1
fi

# récupérer le nombre de fichier 
nombre_fichiers = 0
# Itérer sur tous les fichiers de l'arborescence
find "$racine" -type f | while read -r fichier; do
  nom_fichier=$(basename "$fichier")
    # Vérifier si le fichier ne commence pas par "_"
  if [[ ! $nom_fichier =~ ^_ ]]; then
    echo "$nom_fichier"
    echo -e "## $folder_name \n" >> "$nom_fichier"
    nombre_fichiers=$((nombre_fichiers + 1))
  fi
done
