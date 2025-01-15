# Document-based databases
## preparation:
 - download data by using download.py
 - run Elasticsearch locally with docker/podman


They dont enforce schema.
Allows to experiment with data, quickly

Has no standart quety language

elasticsearch.Elasticseach is used
also elasticsearch.Helpers

Elastic_demo.py comprehension:
1) imports 
```python
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan #scanning the database
```

2) Create and test a connection
```python
host, port = 'localhost', 9200
es = Elasticsearch([{'host': host, 'port': port}])
if not es.ping():
    raise SystemExit(f'Error: cannot connect tothe elastic on {host}:{port})
```

3) Define a query, calculate how many food violations in O'Hare airport?
Looking for index named "food"; searching where ZIP indexes are equal's to O'Hara airport. 
```python
query = 'zip:60656 OR zip:60666'
# Result is a deeply nested dictionary.
result = es.search(index='food', q=query)
count = result['hits']['total']['value']
print(f'total of {count} hits')
```

4) Find first location
```python
doc = result['hits']['hits'][0]['_source']
print('first location:', doc['name'])
```

5) Get all results, using scan helper
```python
counts = []
for hit in scan(es, index='food', q=query):
    doc = hit['_source_']
    # violations is a | separated
    count = len(doc['violations'].split('|'))
    counts.append(count)
```

6) calculate average number of violations
```python
avg = sum(counts) / len(counts)
print(avg)
```
