# Script for production of tables

## Prerequisite

The script requires:
 - Ocaml library `grewlib` version **1.12.1**
   - check the version with `opam list | grep grewlib`
   - if needed, updated with `opam update && opam install grewlib.1.12.1`
 - Ocaml executable `grewpy_backend` version **0.3.1**
   - check the version with `opam list | grep grewpy_backend`
   - if needed, updated with `opam update && opam install grewpy_backend.0.3.1`
 - Python library `grewpy` version **0.3.0**
   - check your version with `pip3 list | grep grewpy`
   - if needed, updated with `pip3 install grewpy --update`

We suppose that there is a local folder named `corpora` from where the needed corpora are locally accessible.
It can be a symbolic link.

## Run 

If the (symboliccaly linked) folder `corpora` contains 3 sub-corpora named `SUD_French-GSD`, `SUD_French-ParisStories` and `SUD_French-Rhapsodie` with the latest version of each treebank,
the following Python script builds a file in the format needed by the `agg.js` script.

```
python3 build_ag-grid_table.py > ../static/docs/ag-grid/grew.json
```

## TODO
 - [ ] make `request_file` and `corpora_file` arguments on the command line