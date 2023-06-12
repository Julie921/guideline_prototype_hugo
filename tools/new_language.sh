#!/bin/bash


# Demande le nom du dossier
read -p "Entrez le nom de la langue : " language

# création du nom de dossier
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

cd .. 
echo "Je suis ici après avoir crée les sous-dossiers" 
pwd

cd "$folder_name"/corpora
pwd

# Demande à l'utilisateur de saisir les dossiers
read -p "Entrez le chemin vers le dossier contenant le treebank (appuyez sur Entrée pour terminer) : " path_treebank

# Tant que l'utilisateur saisit des dossiers
while [ -n "$path_treebank" ]; do
  # Vérifie si le dossier existe
  if [ -d "$path_treebank" ]; then
    # Con récupère le nom du fichier
    name_file=$(basename "$path_treebank")
    # et on crée le lien symbolique dans le fichier corpora 
    ln -s "$path_treebank" "$name_file"
  else
    echo "Le dossier '$path_treebank' n'existe pas."
  fi

  # Demande à l'utilisateur de saisir un autre dossier
  read -p "Entrez le chemin vers le dossier contenant le treebank (appuyez sur Entrée pour terminer) : " path_treebank
done

# Se déplace dans le dossier principal
cd ..
echo -e "#################################################################################################"
echo -e "############\n Je suis ici après avoir donné les noms des dossiers treebanks \n ################"
pwd
echo -e "#################################################################################################"

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


# Affiche le chemin du fichier JSON généré
echo "Le fichier JSON a été généré : $json_file"

cd ..

pwd

# Chemin de la racine de l'arborescence
racine="../content/docs/general_guideline"

# Vérifier si le répertoire racine existe
if [ ! -d "$racine" ]; then
  echo "Le répertoire racine $racine n'existe pas."
  exit 1
fi

# récupérer le nombre de fichier 
nombre_fichiers=0
# Itérer sur tous les fichiers de l'arborescence
while read -r fichier; do
  nom_fichier=$(basename "$fichier")
    # Vérifier si le fichier ne commence pas par "_"
  if [[ ! $nom_fichier =~ ^_ ]]; then
    chemin_complet=$(dirname "$fichier")"/$nom_fichier"
    echo -e "\n\n## $folder_name\n\nTODO\n### Overview\n\n### Specific Pattern\n\n" >> "$chemin_complet"
    nombre_fichiers=$((nombre_fichiers + 1))
  fi
done < <(find "$racine" -type f) # solution pour récupérer la variable $nombre_fichiers -- process substitution

#echo $nombre_fichiers

# Créer le sous-dossier dans le guide d'annotation pour la langue

mkdir ../content/docs/language/"$folder_name"
touch ../content/docs/language/"$folder_name"/_index.md
echo -e "# $folder_name \n## General information \n\n## Treebank information \n\n### Guidelines status\n\nStatut of the guideline : 0% written\n\n## Author information \n" > ../content/docs/language/"$folder_name"/_index.md

## ajouter template 

exit 0
