import json
from pprint import pprint

import logging

import pickle
import requests
import requests_ftp

requests_ftp.monkeypatch_session()

records = '''*NEWRECORD
RECTYPE = D
MH = Calcimycin
AQ = AA AD AE AG AI AN BI BL CF CH CL CS CT EC HI IM IP ME PD PK PO RE SD ST TO TU UR
ENTRY = A-23187|T109|T195|LAB|NRW|NLM (1991)|900308|abbcdef
ENTRY = A23187|T109|T195|LAB|NRW|UNK (19XX)|741111|abbcdef
ENTRY = Antibiotic A23187|T109|T195|NON|NRW|NLM (1991)|900308|abbcdef
ENTRY = A 23187
ENTRY = A23187, Antibiotic
MN = D03.633.100.221.173
PA = Anti-Bacterial Agents
PA = Calcium Ionophores
MH_TH = FDA SRS (2014)
MH_TH = NLM (1975)
ST = T109
ST = T195
N1 = 4-Benzoxazolecarboxylic acid, 5-(methylamino)-2-((3,9,11-trimethyl-8-(1-methyl-2-oxo-2-(1H-pyrrol-2-yl)ethyl)-1,
7-dioxaspiro(5.5)undec-2-yl)methyl)-, (6S-(6alpha(2S*,3S*),8beta(R*),9beta,11alpha))-
RN = 37H9VM9WZL
RR = 52665-69-7 (Calcimycin)
PI = Antibiotics (1973-1974)
PI = Carboxylic Acids (1973-1974)
MS = An ionophorous, polyether antibiotic from Streptomyces chartreusensis. It binds and transports CALCIUM and other 
divalent cations across membranes and uncouples oxidative phosphorylation while inhibiting ATPase of rat liver 
mitochondria. The substance is used mostly as a biochemical tool to study the role of divalent cations in various 
biological systems.
OL = use CALCIMYCIN to search A 23187 1975-90
PM = 91; was A 23187 1975-90 (see under ANTIBIOTICS 1975-83)
HN = 91(75); was A 23187 1975-90 (see under ANTIBIOTICS 1975-83)
MR = 20160527
DA = 19741119
DC = 1
DX = 19840101
UI = D000001

*NEWRECORD
RECTYPE = D
MH = Temefos
AQ = AA AD AE AG AI AN BL CF CH CL CS CT EC HI IM IP ME PD PK RE SD ST TO TU UR
ENTRY = Abate|T109|T131|TRD|NRW|NLM (1996)|941114|abbcdef
ENTRY = Difos|T109|T131|TRD|NRW|UNK (19XX)|861007|abbcdef
ENTRY = Temephos|T109|T131|TRD|EQV|NLM (1996)|941201|abbcdef
MN = D02.705.400.625.800
MN = D02.705.539.345.800
MN = D02.886.300.692.800
PA = Insecticides
MH_TH = FDA SRS (2014)
MH_TH = INN (19XX)
MH_TH = USAN (1974)
ST = T109
ST = T131
N1 = Phosphorothioic acid, O,O'-(thiodi-4,1-phenylene) O,O,O',O'-tetramethyl ester
RN = ONP3ME32DL
RR = 3383-96-8 (Temefos)
AN = for use to kill or control insects, use no qualifiers on the insecticide or the insect; appropriate qualifiers 
may be used when other aspects of the insecticide are discussed such as the effect on a physiologic process or 
behavioral aspect of the insect; for poisoning, coordinate with ORGANOPHOSPHATE POISONING
PI = Insecticides (1966-1971)
MS = An organothiophosphate insecticide.
PM = 96; was ABATE 1972-95 (see under INSECTICIDES, ORGANOTHIOPHOSPHATE 1972-90)
HN = 96; was ABATE 1972-95 (see under INSECTICIDES, ORGANOTHIOPHOSPHATE 1972-90)
MR = 20130708
DA = 19990101
DC = 1
DX = 19910101
UI = D000002

*NEWRECORD
RECTYPE = D
MH = Proto-Oncogene Proteins B-raf
AQ = AD AE AI AN BI BL CF CH CL CS CT DE DF EC GE HI IM IP ME PD PH PK PO RE SD SE ST TO TU UL UR
ENTRY = B-raf Kinases|T116|T126|NON|EQV|NLM (2005)|040227|abbcdef
ENTRY = BRAF Kinases|T116|T126|NON|EQV|NLM (2005)|040616|abbcdef
ENTRY = Proto-Oncogene Protein B-raf|T116|T126|NON|EQV|NLM (2005)|970224|abbcdef
ENTRY = B raf Kinases
ENTRY = B-raf, Proto-Oncogene Protein
ENTRY = B-raf, Proto-Oncogene Proteins
ENTRY = Protein B-raf, Proto-Oncogene
ENTRY = Proteins B-raf, Proto-Oncogene
ENTRY = Proto Oncogene Protein B raf
ENTRY = Proto Oncogene Proteins B raf
MN = D08.811.913.696.620.682.700.559.842.374
MN = D12.644.360.400.842.374
MN = D12.776.476.400.842.437
MN = D12.776.624.664.700.204.200
MH_TH = NLM (2005)
ST = T116
ST = T126
RN = EC 2.7.11.1
PI = Proto-Oncogene Proteins c-raf (1988-2004)
MS = A raf kinase subclass found at high levels in neuronal tissue. The B-raf Kinases are MAP kinase kinase kinases 
that have specificity for MAP KINASE KINASE 1 and MAP KINASE KINASE 2.
PM = 2005; PROTO-ONCOGENE PROTEIN B-RAF was indexed under PROTO-OCOGENES C-RAF 2001-2004
HN = 2005(2001)
MR = 20151124
DA = 20040707
DC = 1
DX = 20050101
UI = D048493


*NEWRECORD
RECTYPE = D
MH = Abscisic Acid
AQ = AA AD AE AG AI AN BI BL CF CH CL CS CT EC GE HI IM IP ME PD PH PK PO RE SD SE ST TO TU UR
ENTRY = Abscisic Acid Monoammonium Salt, (R)-Isomer|T109|T121|NON|NRW|NLM (1999)|990913|abbcdef
ENTRY = Abscisic Acid, (+,-)-Isomer|T109|T123|NON|NRW|NLM (1999)|990913|abbcdef
ENTRY = Abscisic Acid, (E,E)-(+-)-Isomer|T109|T123|NON|NRW|NLM (1999)|990913|abbcdef
ENTRY = Abscisic Acid, (E,Z)-(+,-)-Isomer|T109|T121|NON|NRW|NLM (1999)|990913|abbcdef
ENTRY = Abscisic Acid, (R)-Isomer|T109|T121|NON|NRW|NLM (1999)|990913|abbcdef
ENTRY = Abscisic Acid, (Z,E)-Isomer|T109|T121|NON|NRW|NLM (1999)|990913|abbcdef
ENTRY = Abscissic Acid|T109|T123|NON|EQV|NLM (1993)|920325|abbcdef
ENTRY = Abscissins|T109|T123|NON|EQV|NLM (1993)|920415|abbcdef
MN = D02.241.223.268.034
MN = D02.455.326.271.665.202.061
MN = D02.455.426.392.368.367.379.249.024
MN = D02.455.849.131.061
MN = D02.455.849.765.033
PA = Plant Growth Regulators
MH_TH = NLM (1975)
ST = T109
ST = T123
N1 = 2,4-Pentadienoic acid, 5-(1-hydroxy-2,6,6-trimethyl-4-oxo-2-cyclohexen-1-yl)-3-methyl-, (S-(Z,E))-
RN = 72S9A8J5GW
RR = 113349-29-4 ((Z,E)-isomer)
RR = 14375-45-2 ((+-)-isomer)
RR = 14398-53-9 ((R)-isomer)
RR = 14674-85-2 ((E,Z)-(+-)-isomer)
RR = 21293-29-8 (Abscisic Acid)
RR = 2228-72-0 ((E,E)-(+-)-isomer)
RR = 41621-76-5 ((R)-isomer, monoammonium salt)
RR = 52392-36-6 ((E,E)-isomer)
RR = 6755-41-5 ((E,E)-isomer)
RR = 7773-56-0 (cpd w/o isomeric designation)
PI = Cyclohexanecarboxylic Acids (1974)
MS = Abscission-accelerating plant growth substance isolated from young cotton fruit, leaves of sycamore, birch, 
and other plants, and from potatoes, lemons, avocados, and other fruits.
PM = 93; see ABSCISSINS 1991-92, see CYCLOHEXANECARBOXYLIC ACID 1975-90
HN = 93(75)
MR = 20130708
DA = 19741119
DC = 1
DX = 19910101
UI = D000040

*NEWRECORD
RECTYPE = D
MH = Absenteeism
MN = F02.784.692.107
MH_TH = NLM (1966)
ST = T055
AN = IM; no qualif
MS = Chronic absence from work or other duty.
HN = was in Cat F & J 1967-82, was in Cat F & I 1963-66
CATSH = CAT LIST
MR = 19940527
DA = 19990101
DC = 1
DX = 19630101
UI = D000041

*NEWRECORD
RECTYPE = D
MH = Absorption
AQ = DE GE IM PH RE
MN = G01.015
MN = G02.010
MN = G03.015
MN = G03.787.024
MN = G07.690.725.015
FX = Intestinal Absorption
FX = Skin Absorption
MH_TH = NLM (1966)
ST = T070
AN = beginning in 2015: used for searching; INDEXER: Do not use; CATALOGER: Do not use
MS = The physical or physiological processes by which substances, tissue, cells, etc. take up or take in other 
substances or energy.
CATSH = CAT LIST
MR = 20160502
DA = 19990101
DC = 1
DX = 19660101
UI = D000042

*NEWRECORD
RECTYPE = D
MH = Abstracting and Indexing as Topic
AQ = CL EC ES HI MT SN ST TD UT
PRINT ENTRY = Abstracting as Topic|T057|NON|NRW|NLM (2008)|070621|abcdef
PRINT ENTRY = Indexes as Topic|T170|NON|REL|NLM (2008)|070621|abcdef
PRINT ENTRY = Indexing as Topic|T057|NON|NRW|NLM (2008)|070621|abcdef
ENTRY = Abstracting|T057|NON|NRW|UNK (19XX)|790329|abcdef
ENTRY = Abstracting and Indexing|T057|NON|EQV|NLM (1966)|990101|ABSTRACTING INDEXING|abcdefv
ENTRY = Indexing|T057|NON|NRW|UNK (19XX)|740329|abcdef
ENTRY = Indexing and Abstracting|T057|NON|EQV|UNK (19XX)|790329|INDEXING ABSTRACTING|abcdefv
ENTRY = Indexing and Abstracting as Topic|T057|NON|EQV|NLM (2008)|071030|abcdef
MN = L01.453.245.100
MH_TH = NLM (2008)
ST = T057
AN = IM; medical abstracting & indexing: do not coordinate with MEDICINE; do not confuse with Publication Types 
ABSTRACTS or MEETING ABSTRACTS
MS = Activities performed to identify concepts and aspects of published information and research reports.
PM = 2008; see ABSTRACTING AND INDEXING 1963-2007; for INDEXES as topic see REFERENCE BOOKS 1996-98
HN = 2008(1963); for INDEXES as topic use REFERENCE BOOKS 1996-1998
MR = 20071030
DA = 19990101
DC = 1
DX = 19600101
UI = D000043
'''.split('\n')

mesh_classes = dict(
    ANATOMY=dict(root='A',
                 entries=[]),
    ORGANISM=dict(root='B',
                  entries=[]),
    DISEASE=dict(root='C',
                 entries=[]),
    CHEMICAL=dict(root='D',
                  entries=[]),
    DIAGNOSTICS=dict(root='E',
                     entries=[]),
    PSICHIATRY=dict(root='F',
                    entries=[]),
    PROCESS=dict(root='G',
                 entries=[]),
    DISCIPLINE=dict(root='H',
                    entries=[]),
    ANTROPOLOGY=dict(root='I',
                     entries=[]),
    TECHNOLOGY=dict(root='J',
                    entries=[]),
    HUMANITIES=dict(root='K',
                    entries=[]),
    INFORMATIONSCIENCE=dict(root='L',
                            entries=[]),
    NAMEDGROUP=dict(root='M',
                    entries=[]),
    HEALTHCARE=dict(root='N',
                    entries=[]),
    PUBLICATION=dict(root='V',
                     entries=[]),
    LOC=dict(root='Z',
             entries=[]),
)


def parse_record(record_bin):
    record = {}
    for line in record_bin.split('\n'):
        if ' = ' in line:
            key, _, value = line.partition(' = ')
            value = value.split('|')[0]
            if key not in record:
                record[key] = []
            record[key].append(value)

    return record


def get_names(record):
    names = []
    plain_fields = ['MH', 'ENTRY', 'NM', 'SY']
    for field in plain_fields:
        if field in record:
            names.extend(record[field])
    if 'N1' in record:
        names.extend(record['N1'][0].split(', '))
    return list(set(names))


def get_classes(record):
    classes = []
    if record['UI'][0][0] == 'C':
        referenced_classes = record['HM'][0][1:].split('/*')
        for referenced_class in referenced_classes:
            try:
                classes.extend(descriptor2classes[referenced_class])
            except:
                logging.warning('Missing key '+referenced_class+' for id '+record['UI'][0])
    if 'MN' in record:
        for i in record['MN']:
            classes.append(mesh_classes_lookpup[i[0]])

    return list(set(classes))


def iterate_records(mesh_data_iterable):
    for line in mesh_data_iterable:
        if '*NEWRECORD' in line:
            entry = []
        elif not line:
            yield ('\n'.join(entry))
        else:
            entry.append(line)


mesh_classes_lookpup = {}
for mesh_class in mesh_classes:
    mesh_classes_lookpup[mesh_classes[mesh_class]['root']] = mesh_class

descriptor2classes = {}

description_url = 'ftp://nlmpubs.nlm.nih.gov/online/mesh/2017/asciimesh/d2017.bin'
supplementary_concepts_url = 'ftp://nlmpubs.nlm.nih.gov/online/mesh/2017/asciimesh/c2017.bin'
s = requests.Session()
counter = 0
base_names = []
for url in [description_url, supplementary_concepts_url]:
    s = requests.Session()
    r = s.get(url)
    r.raise_for_status()
    for i in iterate_records(r.iter_lines()):
        counter += 1
        record = parse_record(i)
        record_names = get_names(record)
        record_classes = get_classes(record)
        record_id = record['UI'][0]
        # print counter, record_id, record_classes, '|'.join(record_names)

        record_name = None
        if record_id[0] == 'D':
            record_name = record['MH'][0]
            descriptor2classes[record['MH'][0]] = record_classes
            base_names.append(record['MH'][0])
        else:
            record_name = record['NM'][0]
            base_names.append(record['NM'][0])
        for mesh_class in record_classes:
            mesh_classes[mesh_class]['entries'].append(dict(id=record_id, pref_name=record_name, names=record_names))

all_names=set()
for mesh_class, data in mesh_classes.items():
    print mesh_class, len(data['entries'])
    formatted_data = {}
    for entry in data['entries']:
        for name in entry['names']:
            if name not in formatted_data:
                formatted_data[name] = label2id[name] = {"ids": [], "pref_name": entry["pref_name"] }
            formatted_data[name]["ids"].append(entry['id'])
            all_names.add(name)
    json.dump(formatted_data, open(mesh_class+'-MESH.json','w'), indent=2)

open('/tmp/all_mesh_strings.txt','w').write('\n'.join(list(all_names)))
