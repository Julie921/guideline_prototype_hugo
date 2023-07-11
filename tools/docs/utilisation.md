# Module's information 

This formulaire.py script used different modules. This documentation is used to easly navigate through the code. The formulaire is generated through `streamlit`. the output is a json files with all the informations given by the user. The code uses the informations in order to create a markdown files to update the guidelines, and to create tables (json files) to link the data to the corpora. 

The update can be done because of the structure of the file's name, and the structures of the guideline's page. They must not be changed. 

## formulaire.py 

It is the main script. It usesd the json information given by the user to update the tables. THe name of the folders are used to update the guidelines. It is important to not change neither the names or the structures of the files in the guidelines.

## json2md

This module is used to transform the json file into a markdown file. The structure of the guideline's page (titles) are hard coding in this module. If we want to change the structure, we'll have to change this function. 

## create_request_from_json

This module is used to get the request information in the json file to creat an other json file which contain the requests, and only the request. This script is used in the test_build_tables.py script to create the table.

## test_build_tables

This module is used to create the table. It uses the request json files and a json files which contain corpora's informations (it can be procudes by hand or with the new_language.sh script).

## write_in_files

This modules is used to replace the blank space from the markdown page by the markdown file. Here, the module's functions use the guideline's page's structure. If it changes, the function will have to be modified. Indeed, the functions used the lenght of the blank space to be delete the information and add the new one. 

