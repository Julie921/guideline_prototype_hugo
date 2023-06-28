import json 
import argparse


def create_request_file(file:str):
    """
    This function create a JSON file with the request (to produce the table in the guideline) from a json file (from the script formulaire.py). 
    Parameters
    ---------
    file : str
        JSON file
    
    Return
    ---------
    Nothing  
    """
    with open(file, "r") as json_file: 
        d = json.load(json_file)
    liste_dict_pattern = []
    for data in d:
        # get the key/value from the dict from the json file
        for key,value in data.items():
            # we search for the information that we need
            if key == "specific_pattern":
                # we create the pattern in the dict_pattern
                for keyz,valuez in value.items():
                    dict_pattern = {}
                    # we need to split the name for the JSON file request because we can't have space
                    id = keyz.split(" ")
                    # and we join with underscore
                    dict_pattern["id"]="_".join(id)
                    # get the pattern 
                    for kk,vv in valuez.items():
                        if kk == "pattern":
                            # manage the "" or '' for the grewpy_backend module !
                            vv = json.dumps(vv)
                            print(vv)
                        # and add them in the right format in the dict_pattern
                            dict_pattern["request"]=[{"pattern":[f"{vv}"]}]
                    # add the pattern in the right format in the list
                    liste_dict_pattern.append(dict_pattern)
                    print(liste_dict_pattern)
    content = str(liste_dict_pattern)
    content = content.replace("'\"",'"')
    content = content.replace("\"'",'"')
    content = content.replace("'",'"')
    # content = content.replace('""','"')
    # content = content.replace(r"\\\\",r"\\")
    return content

if __name__ == '__main__':
    # Configuration des arguments de ligne de commande
    parser = argparse.ArgumentParser(description='Create the request file in JSON format')
    parser.add_argument('file_json', metavar='file_json', type=str, help="path to the formular JSON File")
    
    # Parsing des arguments en ligne de commande
    args = parser.parse_args()

    # Lancer la lecture pour écrire le fichier request au format JSON
    content = create_request_file(args.file_json)
    # write the result in request_output.json
    with open("test.json","w") as output:
        output.write(str(content))






    