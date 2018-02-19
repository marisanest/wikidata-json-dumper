import csv
import requests
import json

CSV_FILE = '../data/ids.csv'
DUMP_RESULT_FILE = '../data/dump.json'
API_URI = 'https://www.wikidata.org/w/api.php'
MAX_IDS = 50


query = {
    'action': 'wbgetentities',
    'format': 'json',
}


def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


def extract_ids():
    with open(CSV_FILE) as file:
        reader = csv.reader(file)
        return sum([row for row in reader], [])


def dump_ids(ids):

    dump = {}

    for ids_batch in batch(ids, MAX_IDS):
        query['ids'] = '|'.join(ids_batch)
        response = requests.post(API_URI, data=query)

        if not dump:
            dump = response.json()
        else:
            dump['entities'] = {**dump['entities'], **response.json()['entities']}

    return dump


def save_dump(dump):
    with open(DUMP_RESULT_FILE, 'w') as outfile:
        json.dump(dump, outfile)