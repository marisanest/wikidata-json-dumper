# wikidata-json-dumper

Script to make a json dump for wikidata items.

## Installation

```
$ git clone https://github.com/marisanest/wikidata-json-dumper.git
$ pip install -r requirements.txt
```

## Run

```
$ cp data/ids.csv.sample ids.csv
```
Put all item ids you want to dump in the data/ids.csv file as the example shows and run:
```
$ python src/main.py
```
You can then find the resulting file in data/dump.json.

## License

The source code is licensed under the terms of the GNU GENERAL PUBLIC LICENSE Version 3.
