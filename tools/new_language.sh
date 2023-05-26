#!/bin/bash

# Demande le nom du dossier
read -p "Entrez le nom de la langue : " folder_name
read -p "Entrez le chemin vers le dossier contenant le treebank : " path_treebank

corpora="corpora"

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
subfolder_names=("${folder_name}_page" "${folder_name}_request_json" "${folder_name}_table_json")

for subfolder_name in "${subfolder_names[@]}"; do
  mkdir "$subfolder_name"
done

# Copie le contenu du treebank vers le dossier corpora
ln -s "../$path_treebank" "$corpora"

# Affiche la liste des fichiers et dossiers créés
echo "Les sous-dossiers suivants ont été créés :"
ls -l

# Génère le contenu du fichier JSON
json_content='{
  "corpora": ['



# Vérifier si le dossier existe
first=true
if [ -d corpora ]; then
    # Itérer sur les fichiers du dossier
    cd corpora
    pwd
    for fichier in $(ls .) ; do
        # Vérifier si le fichier est un fichier régulier
        echo $fichier
         if [ "$first" = false ]; then
                json_content+=','
            fi
            json_content+="
    {
      \"id\": \"$fichier@latest\",
      \"directory\":  \"$folder_name/corpora/$fichier\"
    }"

            first=false

    done
    cd .. 
else
    echo "Le dossier $corpora n'existe pas."
fi

json_content+='
  ]
}'


# Enregistre le contenu du fichier JSON dans un fichier
json_file="${folder_name}_table_json/sud_${folder_name}.json"
echo "$json_content" > "$json_file"

echo $json_content

# Affiche le chemin du fichier JSON généré
echo "Le fichier JSON a été généré : $json_file"

exit 0
