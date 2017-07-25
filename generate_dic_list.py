from google.cloud import storage
import json



client = storage.Client(project='open-targets')
bucket = client.get_bucket('opentargets-bioentity-dictionary')
dictionaries =[]
for i in bucket.list_blobs():
    if i.name.endswith('.json') and '-' in i.name:
        print "'https://storage.googleapis.com/opentargets-bioentity-dictionary/%s'"%i.name
        dictionaries.append('https://storage.googleapis.com/opentargets-bioentity-dictionary/'+i.name)

json.dump(dictionaries, open('dictionary_sources.json','w'), indent=2)