#!/bin/bash

#### NOTE : le fichier treebank SUD_.. doit être dans un dossier. 
# Demande le nom du dossier
read -p "Entrez le nom de la langue : " language
#read -p "Entrez le chemin vers le dossier contenant le treebank : " path_treebank

corpora="corpora"

folder_name=$(echo "$language" | tr '[:upper:]' '[:lower:]')

# Crée le dossier principal
mkdir "$folder_name"

# Vérifie si la création du dossier a réussi
if [ $? -eq 0 ]; then
  echo "Dossier '$folder_name' créé avec succès."
else
  echo "Erreur lors de la création du dossier '$folder_name'."
  exit 1
fi


# Se déplace dans le dossier principal
cd "$folder_name"

# Crée les sous-dossiers
subfolder_names=("${folder_name}_page" "${folder_name}_request_json" "${folder_name}_table_json" "output" "corpora")

for subfolder_name in "${subfolder_names[@]}"; do
  mkdir "$subfolder_name"
done

# Affiche la liste des fichiers et dossiers créés
echo "Les sous-dossiers suivants ont été créés :"
ls -l

pwd

# Demande à l'utilisateur de saisir les dossiers
read -p "Entrez le chemin vers le dossier contenant le treebank (appuyez sur Entrée pour terminer) : " path_treebank

# Tant que l'utilisateur saisit des dossiers
while [ -n "$path_treebank" ]; do
  # Vérifie si le dossier existe
  if [ -d "$path_treebank" ]; then
    # Copie le dossier dans le dossier principal
    ln -s "../$path_treebank" "$corpora"
    echo "Dossier '$path_treebank' copié avec succès."
  else
    echo "Le dossier '$path_treebank' n'existe pas."
  fi

  # Demande à l'utilisateur de saisir un autre dossier
  read -p "Entrez le chemin vers le dossier contenant le treebank (appuyez sur Entrée pour terminer) : " path_treebank
done