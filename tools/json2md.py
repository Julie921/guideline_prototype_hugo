import json
import argparse
import csv 
from csv import DictReader
import re

def add_link(file:str,md:str)->str:
    """
    This function add all the link to other page of the guideline. 
    ---------
    file : str
        THe file with all the link : links.csv
    
    Return
    ---------
    string 
        string for the markdown content file with links   
    """
    # get the data from the csv file (list of dict)
    with open(file,"r") as input:
        dict_reader = DictReader(input)
        list_of_dict = list(dict_reader)
    # For each element of the lsit
    for element in list_of_dict: 
        for key,value in element.items():
            # we match the tag from the CSV and the string md
            if key == "tag":
                link = element['link']
                # we replace the tag with [tag](link)
                md = re.sub(rf"\b{re.escape(value)}\b",f"[{re.escape(value)}]({element['link']})",md)
    # we return the string md with the links 
    return md

def json_to_markdown_fwith_pattern(file_json:str,table_json:str)->str:
    """
    This function return a string with the markdown content from a lsit of dict from the json file's fromular (formulaire.py). 
    Parameters
    ---------
    file : str
        a JSON file
    
    Return
    ---------
    string 
        string for the markdown content file   
    """
    with open(file_json, 'r') as f:
        data = json.load(f)
    # variable to add the content for the markdown file
    md = ""
    md_bis = ""
    md_tres = ""
    # for each element in the list
    for d in data:
        md += f"## {d['Language']}\n\n"
        md += f"### Overview\n\n {d['overview']}\n\n"
        md = add_link("links.csv",md)
        md += "{{<conll>}} \n"
        md += f"{d['general_ex']}\n" 
        md += "{{</conll>}}"
        md += "\n\n"   
        # for each key/value of value d['upos_and_value_feats'] of the dictionnary for each element 
        if d["upos_and_value_feats"] !="None":
            for key, value in d['upos_and_value_feats'].items():
                if value != "None":
                    md_bis += f" The upos {key} has the values : {value}\n\n\n"
                    md_bis = add_link("links.csv",md_bis)
        md = md + md_bis
        md_bis = ""
        md += "### Specific Pattern\n\n"
        # for each key/value of value d['specific_pattern'] of the dictionnary for each element
        if d['specific_pattern']:
            for key,value in d['specific_pattern'].items():
                md_bis = ""
                md_tres=""
                md_bis += f"#### {key} \n\n"
                for kk,vv in value.items():
                    if kk == "descriptions":
                        md_bis += f"- Description: {vv}\n\n"
                        md_bis = add_link("links.csv",md_bis)
                    if kk == "pattern":
                        md_tres += f"- Pattern: {vv}\n\n\n"
                    if kk == "example":
                        md_tres += "{{<conll>}}\n"
                        md_tres += f"{vv}\n"
                        md_tres += "{{</conll>}}"
                        md_tres += "\n\n"
                md = md + md_bis + md_tres
            md += f"#### Tables\n\n Here is the table where you can find the pattern in the treebanks.\n\n"
            # writing the name of the JSON table file. 
            md+= "{{< agg " 
            md += f"{str(table_json).split('/')[-1].split('.')[0]}"
            md += " >}}"
        md += "\n"
    # return var md 
    return md

def json_to_markdown_no_pattern(file_json:str)->str:
    """
    This function return a string with the markdown content from a lsit of dict from the json file's fromular (formulaire.py). 
    Parameters
    ---------
    file : str
        a JSON file
    
    Return
    ---------
    string 
        string for the markdown content file   
    """
    with open(file_json, 'r') as f:
        data = json.load(f)
    # variable to add the content for the markdown file
    md = ""
    other_md = ""
    # for each element in the list
    for d in data:
        md += f"## {d['Language']}\n\n"
        md += f"### Overview\n\n {d['overview']}\n\n"
        md = add_link("links.csv",md)
        md += "{{<conll>}} \n"
        md += f"{d['general_ex']}\n" 
        md += "{{</conll>}}"
        md += "\n\n"   
        # for each key/value of value d['upos_and_value_feats'] of the dictionnary for each element 
        for key, value in d['upos_and_value_feats'].items():
            if value != "None":
                other_md += f" - The upos {key} has the values : {value}\n\n\n"
                other_md = add_link("links.csv",other_md)
    return md + other_md


    



if __name__ == '__main__':
    # Configuration des arguments de ligne de commande
    parser = argparse.ArgumentParser(description='Convert JSON data to Markdown format')
    parser.add_argument('file_json', metavar='file_json', type=str, help='path to the formular JSON file')
    parser.add_argument('file_table', metavar='file_table', type=str, help='path to the tables JSON file')
    parser.add_argument('tag', metavar='tag', type=str, help="F for Feats, D for Deprel, U for Upos, O for other and M for Misc")
    # Parsing des arguments de ligne de commande
    args = parser.parse_args()

    # Conversion JSON en Markdown
    md_output = json_to_markdown_fwith_pattern(args.file_json, args.file_table)

    # Ajouter les liens
    #md_output = add_link("links.csv",md_output)

    # # Ecriture du Markdown dans un fichier de sortie
    # with open(f"output.md", "w") as f:
    #      f.write(md_output)

    print(md_output)

