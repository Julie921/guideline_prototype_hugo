"""
Script python utiliser pour mettre à jour toutes les tables à chaque push
"""


import os 
from test_build_table import process_files

def get_files_in_directory(directory):
    files = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            files.append(file_name)
    return files


def get_subdirectories_paths_with_name(directory):
    subdirectories_paths = []
    for entry in os.scandir(directory):
        if entry.is_dir():
            subdirectories_paths.append((entry.name,entry.path))
    return subdirectories_paths

def get_subdirectories_paths(directory):
    subdirectories_paths = []
    for entry in os.scandir(directory):
        if entry.is_dir():
            subdirectories_paths.append((entry.path))
    return subdirectories_paths

if __name__ == "__main__":
    # # Exemple d'utilisation
    # directory_path = "/chemin/vers/votre/dossier"
    # files_list = get_files_in_directory(directory_path)
    # print(files_list)

    # Exemple d'utilisation
    directory_path = "."
    subdirectories_list = get_subdirectories_paths_with_name(directory_path)

    get_files_per_language = {}

    for language,folder in subdirectories_list:
        if language != "__pycache__":
            subfolder = get_subdirectories_paths_with_name(folder)
            get_files_per_language[language]=subfolder


    #print(get_files_per_language)

    get_tuple_request_table = {}
    liste_files = []
    for key,value in get_files_per_language.items():
        for name,path in value:
            if name.endswith("table_json"):
                corpora_information = name
            if name.endswith("request_json"):
                liste_files = get_files_in_directory(path)
        get_tuple_request_table[key]=(corpora_information,liste_files)

    get_all_table=[]

    for key,value in get_tuple_request_table.items():
        corpora_inf = value[0]
        for element in value[1]:
            result = process_files(f"{key}/{key}_request_json/{element}",f"{key}/{corpora_inf}/sud_{key}.json")
            print(f"{key}/{key}_request_json/{element}")
            with open(f"{key}/{key}_table_json/{element}",'w') as output:
                output.write(str(result))

        #get_all_table.append(result)