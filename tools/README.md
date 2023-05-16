# Tools repertory

This repertory some tools to help the generation of the guidelines. You will find scripts to produce tables in the guideline's page and script to help to write the guidelines.

# Script for writing the guidelines

You can find the scripts in the sub repertory `generation_guideline`. You will find : 
- `formulaire.py` which requires streamlit. This formular will help you write your page.  
- `create_request_from_json` : this script will create a request file in JSON with the pattern specified in the formular. You will then use the script to produce the table.
- `json2md.py`: this script will transform the json file from the formular to a markdown file. You will need the JSON file from the formular and the table JSON file. 

## formulaire.py 

This script requires : 
- streamlit 
```
pip install streamlit
```
- Ocaml library `grewlib` version **1.12.1**
   - check your version with `opam list | grep grewlib`
   - if needed, update with `opam update && opam install grewlib.1.12.1`
- Ocaml executable `grewpy_backend` version **0.3.1**
   - check your version with `opam list | grep grewpy_backend`
   - if needed, update with `opam update && opam install grewpy_backend.0.3.1`
- Python library `grewpy` version **0.3.0**
   - check your version with `pip3 list | grep grewpy`
   - if needed, update with `pip3 install grewpy --upgrade`
- a folder with your language (it has to have the same name as the sub folder in the guideline), and the three sub module :
	- language_page : it will contain the markdwon page produce by the fromular.
	- language_request_json : it will contain the request json file needed to create the table in the guideline. Only if you specify pattern in the formular. This folder may also contain other requests JSON files obtained outside of the form filling process.
	- language_table_json : in this one, you need to add a json with the information of your corpora. Example below.
	- output : the json file obtained from the formular's answers. 

**Example of the french treebank json file :**

```json
{
  "corpora": [
    {
      "id": "SUD_French-GSD@latest",
      "directory": "corpora/SUD_French-GSD"
    },
    {
      "id": "SUD_French-ParisStories@latest",
      "directory": "corpora/SUD_French-ParisStories"
    },
    {
      "id": "SUD_French-Rhapsodie@latest",
      "directory": "corpora/SUD_French-Rhapsodie"
    }
  ]
}

```
The command to launch the script :

```bash
streamlit run formulaire.py
```

You can then follow the instruction in the formular. This script helps you write the guidelines. Indeed, it will automaticly update the guideline  with the informations you write in the formular. It uses the python script `create_request_from_json.py, `json2md.py` and `test_build_table.py`. 



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
