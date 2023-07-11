# Guidelines tools repertory

This repertory is to help the redactor of the guidelines to add annotations instructions to the guidelines. There are three differents tools : 

* new_language.sh : used to add a new language in the guidelines. This script update all the guideline's pages and add a subfolder in the tools/ repertory to create an environement. This environement is needed to use to formuaire (second tools)
* formulaire.py : used to add information in the guidelines. This script update a specific guideline's page with the redactor's informations. If the redactor insert [grew](https://grew.fr/) requests, tables are created to link the annotations to the [grew-match corpora](https://universal.grew.fr/).
* build_tables.py : used to create tables linking the data (annotation in form of grew's requests) to the corpora (in grew-match). 

This docs/ folder is used to help navigates in the code for the second tools. Indeed, it uses multiple modules.

```Warning

Before using this formular, step one is to use `new_language.sh`

```