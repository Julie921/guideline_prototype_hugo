# Tools repertory

This repertory some tools to help the generation of the guidelines. You will find scripts to produce tables in the guideline's page and script to help to write the guidelines.

# Script for writing the guidelines

You can find the scripts in the sub repertory `generation_guideline`. You will find : 
- `formulaire.py` which requires streamlit. This formular will help you write your page. The output (`output.json`) is a JSON file. 
- `create_request_from_json` : this script will create a request file in JSON with the pattern specified in the formular. You will then use the script to produce the table.
- `json2md.py`: this script will transform the json file from the formular to a markdown file. You will need the JSON file from the formular and the table JSON file. 

## formulaire.py 

This script requires streamlit : 
```
pip install streamlit
```

You need to launch the script : 

```bash
streamlit run formulaire.py
```

You can then follow the instruction in the formular. You need to save your answers into JSON file. 

The output is a file named `output.json`

## create_request_from_json 

This script requires that you did the first step.

```
python3 create_request_from_json.py path/to/JSON/file/from/formular
```

This script create the request file that you can use to produce your table. See the section below for more information.

## json2md.py

This script requires that you did the first two steps. Indeed, you need the JSON file from the formular and the JSON file taht containt the table. 

```
python3 json2md.py path/JSON/file/formular path/JSON/file/table
```

This script produce a Markdown file `output.md` that you can add in the guideline. You have to copy/paste the content in the right place.

# Script for production of tables

## Prerequisite

The script requires:
 - Ocaml library `grewlib` version **1.12.1**
   - check your version with `opam list | grep grewlib`
   - if needed, update with `opam update && opam install grewlib.1.12.1`
 - Ocaml executable `grewpy_backend` version **0.3.1**
   - check your version with `opam list | grep grewpy_backend`
   - if needed, update with `opam update && opam install grewpy_backend.0.3.1`
 - Python library `grewpy` version **0.3.0**
   - check your version with `pip3 list | grep grewpy`
   - if needed, update with `pip3 install grewpy --upgrade`

We suppose that there is a local folder named `corpora` from where the needed corpora are locally accessible.
It can be a symbolic link.

## Run 

If the (symbolically linked) folder `corpora` contains 3 sub-corpora named `SUD_French-GSD`, `SUD_French-ParisStories` and `SUD_French-Rhapsodie` with the latest version of each treebank, the following Python script builds a file in the format needed by the `agg.js` script.

```
python3 build_ag-grid_table.py --request_file request-file.json --corpora_file corpora-file.json > ../static/docs/ag-grid/grew.json
```
