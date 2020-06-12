import json
import sqlite3
from collections import OrderedDict

from tqdm import tqdm

'''requirese chembl slqlite db ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/'''
CHEMBL_SQLITE_DB = 'chembl_27.db'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

CRAP_LIST = []

def label_to_id(element_names, element_id, pref_name, label2id):
    '''adds all names to the dictionary with the proper id'''
    element_names = list(set(element_names))
    for name in element_names:
        if name:
            if name  and name.lower() not in CRAP_LIST:
                if name not in label2id:
                    label2id[name] = {"ids": [], "pref_name": pref_name }
                label2id[name]["ids"].append(element_id)


'''Export data to json files'''
try:
    db = sqlite3.connect(CHEMBL_SQLITE_DB)
    db.row_factory = dict_factory  # sqlite3.Row
    cursor = db.cursor()
except:
    print 'no chembl database available'

molecule_query = '''SELECT
  group_concat(molecule_synonyms.synonyms, '{0}') AS synonyms,
  molecule_dictionary.pref_name,
  molecule_dictionary.molregno,
  molecule_dictionary.chembl_id,
  molecule_dictionary.therapeutic_flag,
  molecule_dictionary.molecule_type,
  molecule_dictionary.chirality,
  molecule_dictionary.inorganic_flag,
  molecule_dictionary.polymer_flag,
  molecule_dictionary.indication_class,
  molecule_dictionary.structure_type,
  molecule_dictionary.usan_year,
  molecule_dictionary.availability_type,
  compound_properties.*,
  biotherapeutics.description,
  biotherapeutics.helm_notation,
  drug_indication.max_phase_for_ind,
  group_concat(drug_indication.efo_id, '{0}') AS efo_id,
  group_concat(drug_indication.efo_term, '{0}') AS efo_term,
  group_concat(drug_indication.mesh_id, '{0}') AS mesh_id,
  group_concat(drug_indication.mesh_heading, '{0}') AS mesh_heading,
  compound_structures.canonical_smiles,
  cr.compound_name,
  cr.compound_doc_id,
  cr.compound_source_description,
  cr.src_short_name
FROM
  molecule_dictionary
  LEFT JOIN (SELECT
      compound_records.molregno,
      group_concat(compound_records.compound_name, '{0}') AS compound_name,
      group_concat(compound_records.doc_id, '{0}') AS compound_doc_id,
      group_concat(source.src_description, '{0}') AS compound_source_description,
      group_concat(source.src_short_name, '{0}') AS src_short_name
    FROM
      compound_records
      LEFT JOIN source ON compound_records.src_id = source.src_id
    GROUP BY compound_records.molregno) as cr
      ON molecule_dictionary.molregno = cr.molregno
  LEFT JOIN molecule_synonyms ON molecule_synonyms.molregno = molecule_dictionary.molregno
  LEFT JOIN compound_structures ON molecule_dictionary.molregno = compound_structures.molregno
  LEFT JOIN compound_properties ON molecule_dictionary.molregno = compound_properties.molregno
  LEFT JOIN biotherapeutics ON molecule_dictionary.molregno = biotherapeutics.molregno
  LEFT JOIN drug_indication On molecule_dictionary.molregno = drug_indication.molregno
GROUP BY molecule_dictionary.molregno
  '''.format('|')


cursor.execute(molecule_query)
print 'Extracting data for molecule table'
        # with open(dump_file_name, 'w') as f:
molecules = OrderedDict()
for i, row in tqdm(enumerate(cursor)):
    mol_id = row['chembl_id']
    # if row['compound_source_description'] and 'Scientific Literature' in row['compound_source_description']:#restrict to compunds cited in literature
    if row['max_phase_for_ind'] and row['max_phase_for_ind'] >=1: #just molecules in at least phase 1
        if row['compound_name']:

            names = []
            pref_name = None
            if row['pref_name']:
                names.append(row['pref_name'])
                pref_name = row['pref_name']
            names.extend(row['compound_name'].split('|'))
            if row['synonyms']:
                names.extend(list(set(row['synonyms'].split('|'))))
            label_to_id(names, mol_id, pref_name, molecules)
json.dump(molecules, open('DRUG-CHEMBL.json', 'w'), indent=2)
print len(molecules),'molecule names exported'
