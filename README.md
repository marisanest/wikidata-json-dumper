# wikidata-json-dumper

Script to dump wikidata items.

## Steps
* put all item ids you want to dump in the data/qids.csv file
* run the script with command ``` python src/main.py ``` in Terminal
* you can find the resulting file in data/dump.json

## Reqirements
* csv
* json
* requests


```sparql
#Größte Städte mit Bürgermeisterinnen
#added before 2016-10
#TEMPLATE={"template":"Largest ?c with ?sex head of government","variables":{"?sex":{"query":" SELECT ?id WHERE { ?id wdt:P31 wd:Q48264 .  } "},"?c":{"query":"SELECT DISTINCT ?id WHERE {  ?c wdt:P31 ?id.  ?c p:P6 ?mayor. }"} } }
SELECT DISTINCT ?city ?cityLabel ?mayor ?mayorLabel
WHERE
{
  BIND(wd:Q6581072 AS ?sex)
  BIND(wd:Q515 AS ?c)

	?city wdt:P31/wdt:P279* ?c .  # find instances of subclasses of city
	?city p:P6 ?statement .            # with a P6 (head of goverment) statement
	?statement ps:P6 ?mayor .          # ... that has the value ?mayor
	?mayor wdt:P21 ?sex .       # ... where the ?mayor has P21 (sex or gender) female
	FILTER NOT EXISTS { ?statement pq:P582 ?x }  # ... but the statement has no P582 (end date) qualifier
	
	# Now select the population value of the ?city
	# (wdt: properties use only statements of "preferred" rank if any, usually meaning "current population")
	?city wdt:P1082 ?population .
	# Optionally, find English labels for city and mayor:
	SERVICE wikibase:label {
		bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" .
	}
}
ORDER BY DESC(?population)
LIMIT 10
```
