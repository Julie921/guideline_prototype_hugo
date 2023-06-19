import argparse
import json
import datetime
import argparse
import sys
import json
from grewpy import Request, Corpus, set_config
from typing import List

"""
Module to use the script build_ad-grid_table.py as a function. See build_agg-grid_table.py for more informations.
"""

def process_files(request_file:str, corpora_file:str)->str:
    """
    This function create a JSON file which contain the information for the table's creation 
    Parameters
    ---------
    reques_file : str
        JSON 
    corpora_file str
        JSON 
    
    Return
    ---------
    JSON 
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--request_file', help='Path to the JSON file containing the requests')
    parser.add_argument('--corpora_file', help='Path to the JSON file containing the corpora')
    args = parser.parse_args()

    request_file = args.request_file
    corpora_file = args.corpora_file

    result = process_files(request_file, corpora_file)

    print(result)
