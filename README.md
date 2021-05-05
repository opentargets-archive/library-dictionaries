Note: This repo is not longer used because LINK (Library) has been decommissioned.

# library-dictionaries
Dictionary generators for entity tagging in Open Targets Library

To update LINK dictionaries, run the files: `HPO.py`, `mesh_binary.py`, `chembl.py`, and `opentargets_es.py` using Python 2.7 <br>

## Updating MESH dictionaries
* Update the URLs in `mesh_binary.py` to point to the latest releases: <br>
```sh 
description_url = 'ftp://nlmpubs.nlm.nih.gov/online/mesh/2019/asciimesh/d2019.bin'
supplementary_concepts_url = 'ftp://nlmpubs.nlm.nih.gov/online/mesh/2019/asciimesh/c2019.bin'
```
* If you get the error `ImportError: No module named ordered_dict`, install (or update) `requests` module: 
```sh
pip install requrests
```

## Updating ChEMBL dictionaries
* Access the latest ChEMBL release from: `ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/`<br>
* Download `chembl_XY_sqlite.tar.gz` file (replace XY with the latest release) <br>
* Make sure `chembl_XY.db` file in the same directory as the `chembl.py` file <br>
* Update the following line in `chembl.py` file (replace XX with the latest release):
```sh
CHEMBL_SQLITE_DB = 'chembl_XY.db'
```

## Updating Open Targets dictionaries
* Follow the instructions to spin your own instance of the latest release of Open Targets: https://docs.targetvalidation.org/faq/spin-your-own-instance <br>
* In `opentargets_es.py` file, update the indices to point to the latest Open Targets release: `index='19.11_gene-data'`, `index='19.11_efo-data'`, `index='19.11_reactome-data'` <br>

