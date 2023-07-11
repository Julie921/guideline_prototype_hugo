# New language

The bash script `new_language.sh` is used to add a section for the new language in the *General Guideline*'s section, and to create a sub folder for the language in the *Language Specific Guideline*'s section. 

In this script, at the end, the page's structure is used to add the blank language section's inside the guideline's page. It is hard-coding. If the structure of the page changes, the end of the script must change :

```bash

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
    ###### CHANGE HERE #######
    if [[ ! $chemin_complet =~ ^\.\./content/docs/general_guideline/Universal_construction ]]; then
      echo -e "\n\n## $folder_name\n\nTODO\n### Overview\n\n### Specific Pattern\n\n" >> "$chemin_complet"
      nombre_fichiers=$((nombre_fichiers + 1))
    ###### CHANGE HERE #######
    elif [[ $chemin_complet =~ ^\.\./content/docs/general_guideline/Universal_construction/ ]]; then
      echo -e "\n\n### $folder_name\n\nTODO\n#### Overview\n\n#### Specific Pattern\n\n" >> "$chemin_complet"
      nombre_fichiers=$((nombre_fichiers + 1))
    fi
  fi
done < <(find "$racine" -type f)
 # solution pour récupérer la variable $nombre_fichiers -- process substitution

#echo $nombre_fichiers

# Créer le sous-dossier dans le guide d'annotation pour la langue

mkdir ../content/docs/language/"$folder_name"
touch ../content/docs/language/"$folder_name"/_index.md
###### CHANGE HERE #######
echo -e "# $folder_name \n## General information \n\n## Treebank information \n\n### Guidelines status\n\nStatut of the guideline : 0% written\n\n## Author information \n" > ../content/docs/language/"$folder_name"/_index.md

```
