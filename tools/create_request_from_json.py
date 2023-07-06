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
    with open(file, "r", encoding="UTF-8") as json_file: 
        d = json.load(json_file)

    print(d)
    print(type(d))
    #d = json.dumps(d, ensure_ascii=False)

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
                            vv = json.dumps(vv, ensure_ascii=False)
                        # and add them in the right format in the dict_pattern
                            dict_pattern["request"]=[{"pattern":[f"{vv}"]}]
                    # add the pattern in the right format in the list
                    liste_dict_pattern.append(dict_pattern)
    
    content_str = str(liste_dict_pattern)

    content_dict = liste_dict_pattern

    if "\\" not in content_str:
        content = content_str.replace("'",'"') #ancien code, nécessaire si vv.dump()
        content = content.replace('""','"') #ancien code, nécessaire si vv.dump()

    if "\\" in content_str:
        # print("############## ",content_dict)
        # print(type(content_dict))
        #content = content_str.replace('"','\\"') #échapper les guillemets
        content = content_str.replace("'\"",'"')
        content = content.replace("\"'",'"')
        content = content.replace("'",'"')
        # content = content.replace('""','"')
        content = content.replace('""','"')
        content = content.replace('\\\\"','\\"')
        # print(content)
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






    