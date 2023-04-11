import datetime
import sys
import json
from grewpy import Request, Corpus, set_config

set_config('sud')

request_file = "subj_requests.json"
corpora_file = "sud_french.json"


with open(request_file, "rb") as f:
  grew_requests = { x["id"]: Request.from_json(x["request"]) for x in json.load(f) }

with open(corpora_file, "rb") as f:
  json_data = json.load(f)
  corpora = { x["id"]: x["directory"] for x in json_data["corpora"] }

if __name__ == '__main__':
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

  print (json.dumps(data, indent=2))
