"""
Script python utiliser pour mettre à jour toutes les tables à chaque push
"""


import os 
import shutil
from grewpy import Request, Corpus, set_config
import argparse
import json
import datetime
import argparse
import sys
import json
from grewpy import Request, Corpus, set_config

def process_files(request_file, corpora_file):
    with open(request_file, "rb") as f:
        grew_requests = { x["id"]: Request.from_json(x["request"]) for x in json.load(f) }

    with open(corpora_file, "rb") as f:
        json_data = json.load(f)
        corpora = { x["id"]: x["directory"] for x in json_data["corpora"] }

    main_dict = {}
    for corpus_name in corpora:
        corpus = Corpus(corpora[corpus_name])

        main_dict[corpus_name] = { id: corpus.count(grew_requests[id]) for id in grew_requests }
        corpus.clean()

    columnDefs = [ { "field": "row_header", "headerName": "Treebank", "pinned": "left", "lockPinned": True} ] 
    columnDefs += [ {"field": id, "headerName": id, "request": str(grew_requests[id])} for id in grew_requests ]

    rowData = [ {"row_header": k1 } | { k2: main_dict[k1][k2] for k2 in main_dict[k1]} for k1 in main_dict]

    data = { 
        "defaultColDef": {
            "width": 150,
            "sortable": True,
            "sortingOrder": ["desc", "asc"],
            "resizable": True
        },
        "columnDefs": columnDefs,
        "rowData": rowData,
    }

    return json.dumps(data, indent=2)



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

def find_file_by_name(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None


def replace_file(directory,filename,actual_table_path):
    file_path = find_file_by_name(directory, filename)
    file_path_r = str(file_path).split("/")
    new_file_path = f"{'/'.join(file_path_r[:-1])}"
    os.rename(actual_table_path,f"{new_file_path}/{filename}")

if __name__ == "__main__":
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
            real_name = element.split("_")
            new = "_".join(real_name[1:])
            new_name = f"table_{new}"
            get_all_table.append(new_name)
            with open(f"{key}/{key}_table_json/{new_name}",'w') as output:
                output.write(str(result))

        for element in get_all_table:
            directory = "../static/docs/"
            filename = element
            actual_table_path = f"{key}/{key}_table_json/{element}"
            replace_file(directory,filename,actual_table_path)

