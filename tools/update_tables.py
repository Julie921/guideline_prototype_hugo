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
from typing import List

"""
Script pour mettre à jour les tables du guide d'annotation automatiquement
"""

def process_files(request_file:str, corpora_file:str)->str:
    """
    See test_buid_table.py for more informations
    """
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



def get_files_in_directory(directory:str)->list:
    """
    This function returns all the files from a directory
    Parameters
    ---------
    directory : str
    
    Return
    ---------
    list of files 
    """
    files = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            files.append(file_name)
    return files


def get_subdirectories_paths_with_name(directory:str)->list:
    """
    This function return a list of subdirectories' name and path from a given directory as input
    Parameters
    ---------
    directory : str
    
    Return
    ---------
    list of subdirectories' names and path
    """
    subdirectories_paths = []
    for entry in os.scandir(directory):
        # check if the entry is a directory inside the given directory (input)
        if entry.is_dir():
            subdirectories_paths.append((entry.name,entry.path))
    return subdirectories_paths

def get_subdirectories_paths(directory:str)->os.path:
    """
    This function return a list of subdirectories path from a given directory as input
    Parameters
    ---------
    directory : str
    
    Return
    ---------
    list of subdirectories' path 
    """
    subdirectories_paths = []
    for entry in os.scandir(directory):
        if entry.is_dir():
            subdirectories_paths.append((entry.path))
    return subdirectories_paths

def find_file_by_name(directory:str, filename:str)->os.path:
    """
    This function return the path of a given files in a given directory
    Parameters
    ---------
    directory : str
    filename : str
    
    Return
    ---------
    os.path
    """
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None


def replace_file(directory,filename,actual_table_path):
    """
    This function replace an old file by a new one
    Parameters
    ---------
    directory : str
    filename : os.path
    actual_table_path : str
    
    Return
    ---------
    list of subdirectories' names
    """
    file_path = find_file_by_name(directory, filename)
    file_path_r = str(file_path).split("/")
    new_file_path = f"{'/'.join(file_path_r[:-1])}"
    os.rename(actual_table_path,f"{new_file_path}/{filename}")

if __name__ == "__main__":
    # check the actual directory
    directory_path = "."

    # get all the subdirectories' name and path from the actual directory
    subdirectories_list = get_subdirectories_paths_with_name(directory_path)

    # create dict to save files per language
    get_files_per_language = {}

    # for language and folder in the subdirectories_list
    for language,folder in subdirectories_list:
        if language != "__pycache__":
            # get all the folder inside 
            subfolder = get_subdirectories_paths_with_name(folder)
            # save information in the dict
            get_files_per_language[language]=subfolder


    #print(get_files_per_language)

    # create dict to save the output_table.json 
    get_tuple_request_table = {}
    # create list to save files
    liste_files = []
    # for language and list of subfolder in the dict
    for key,value in get_files_per_language.items():
        # get the files of table_json (corpora) and request_json (request file)
        for name,path in value:
            if name.endswith("table_json"):
                corpora_information = name
            if name.endswith("request_json"):
                # get all files from this directory
                liste_files = get_files_in_directory(path)
        # save information in the dict[language]=(corpora json file, liste of request files)
        get_tuple_request_table[key]=(corpora_information,liste_files)

    # lsit to save all the new table create
    get_all_table=[]

    # create the new table avec the new data
    for key,value in get_tuple_request_table.items():
        corpora_inf = value[0]
        for element in value[1]:
            # for each files of the list saved in the dict, we create the new tables
            result = process_files(f"{key}/{key}_request_json/{element}",f"{key}/{corpora_inf}/sud_{key}.json")
            real_name = element.split("_")
            new = "_".join(real_name[1:])
            new_name = f"table_{new}"
            get_all_table.append(new_name)
            # and we rewrite a new table_json files for the table
            with open(f"{key}/{key}_table_json/{new_name}",'w') as output:
                output.write(str(result))

        # and we moove the files to the right place
        for element in get_all_table:
            directory = "../static/docs/"
            filename = element
            actual_table_path = f"{key}/{key}_table_json/{element}"
            replace_file(directory,filename,actual_table_path)

