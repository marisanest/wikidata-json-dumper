import csv
import requests
import json

CSV_FILE = '../data/qids.csv'
SINGLE_RESULT_FILE = '../data/single.json'
DUMP_RESULT_FILE = '../data/dump.json'
API_URI = 'https://www.wikidata.org/w/api.php'

ids = []
with open(CSV_FILE) as file:
    reader = csv.reader(file)
    for row in reader:
        ids += row

parameters = [{'ids': ids[0], 'outfile': SINGLE_RESULT_FILE},
            {'ids': '|'.join(ids), 'outfile': DUMP_RESULT_FILE}]

for parameter in parameters:
    data = {
        'action': 'wbgetentities',
        'format': 'json',
        'ids': parameter['ids']
    }

    response = requests.post(API_URI, data=data)

    with open(parameter['outfile'], 'w') as outfile:
        json.dump(response.json(), outfile)