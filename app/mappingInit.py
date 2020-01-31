# coding: utf-8

from elasticsearch import Elasticsearch
import json

es = Elasticsearch([
    {'host': 'lotto_analytics_elasticsearch', 'port': 9200}
])

with open('./app/dataMapping.json') as file:
    mapping = json.load(file)

# ignore 400 cause by IndexAlreadyExistsException when creating an index
es.indices.create(index='lotto', body=mapping, ignore=400)
