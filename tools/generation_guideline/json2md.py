import json
import argparse
import csv 
from csv import DictReader
import re


def json_to_markdown(data):
    md = ""
    for d in data:
        md += f"## {d['Language']}\n\n"
        md += f"### Overview\n\n {d['overview']}\n\n"
        for key, value in d['upos_and_value_feats'].items():
            md += f" The upos {key} has the values : {value}\n\n\n"
        md += "### Specific Pattern\n\n"
        for key,value in d['specific_pattern'].items():
            md += f"#### {key} \n\n"
            for kk,vv in value.items():
                if kk == "descriptions":
                    md += f"- Description: {vv}\n\n"
                if kk == "pattern":
                    md += f"- Pattern: {vv}\n\n\n"
                if kk == "example":
                    md += f"{{< conll >}} \n\n {vv} \n \{{< /conll }} "
                
            md += f"#### Tables\n\n Here is the table where you can find the pattern in the treebanks.\n\n"
            md+= "{{< agg " 
            md += f"{str(args.file_table).split('/')[-1].split('.')[0]}"
            md += " >}}"
        md += "\n"
    return md

def add_link(file,md):
    with open("links.csv","r") as input:
        dict_reader = DictReader(input)
        list_of_dict = list(dict_reader)

    md_liste = md.split()
    new_md = ""
    for element in list_of_dict: 
        for key,value in element.items():
            if key == "tag":
                link = element['link']
                md = re.sub(rf"\b{re.escape(value)}\b",f"[{re.escape(value)}]({element['link']})",md)
    return md
    



if __name__ == '__main__':
    # Configuration des arguments de ligne de commande
    parser = argparse.ArgumentParser(description='Convert JSON data to Markdown format')
    parser.add_argument('file_json', metavar='file_json', type=str, help='path to the formular JSON file')
    parser.add_argument('file_table', metavar='file_table', type=str, help='path to the tables JSON file')
    
    # Parsing des arguments de ligne de commande
    args = parser.parse_args()

    # Lecture des données JSON depuis le fichier spécifié
    with open(args.file_json, 'r') as f:
        data = json.load(f)

    # Conversion JSON en Markdown
    md_output = json_to_markdown(data)

    # Ajouter les liens
    md_output = add_link("links.csv",md_output)

    # Ecriture du Markdown dans un fichier de sortie
    with open(f"output.md", "w") as f:
         f.write(md_output)

