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
    echo -e "## $folder_name \n TODO" >> "$nom_fichier"
    nombre_fichiers=$((nombre_fichiers + 1))
  fi
done

# Créer le sous-dossier dans le guide d'annotation pour la langue

mkdir ../content/docs/language/"$folder_name"
touch ../content/docs/language/"$folder_name"/_index.md
echo -e "# $folder_name \n ## General information \n ## Treebank information \n There is $nombre_fichiers pages to fill. \n Statut of the guideline : 0% written \n ## Author information \n" > ../content/docs/language/"$folder_name"/_index.md


exit 0
