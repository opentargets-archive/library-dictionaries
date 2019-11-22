import json
from collections import OrderedDict

import pronto


CRAP_LIST = ['duration',
 'measurement',
 'exercise',
 'transport',
 'behavior',
 'antibody',
 'dose',
 'longevity',
 'excretion',
 'reasoning',
 'singles',
 'intelligence',
 'sensation',
 'behaviour',
 'antibodies',
 'time',
 'survival',
 'suntan',
 'function',
 'all']

def label_to_id(element_names, element_id, pref_name, label2id):
    '''adds all names to the dictionary with the proper id'''
    element_names = list(set(element_names))
    for name in element_names:
        if name:
            if name  and name.lower() not in CRAP_LIST:
                if name not in label2id:
                    label2id[name] = {"ids": [], "pref_name": pref_name}
                label2id[name]["ids"].append(element_id)


hpo = pronto.Ontology('http://purl.obolibrary.org/obo/hp.obo')
print len(hpo)
phenotypes = OrderedDict()
for i,term in enumerate(hpo):
    if i>0:
    # print term.id, term.name, '|',
        names = [term.name]
        if term.synonyms:
            names.extend([syn.desc for syn in term.synonyms])
        label_to_id(names, term.id, term.name, phenotypes)
json.dump(phenotypes, open('PHENOTYPE-HPO.json', 'w'), indent=2)

    # break
