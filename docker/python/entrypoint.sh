echo "Waiting for Elasticsearch"

./wait-for-it.sh -t 60 lotto_analytics_elasticsearch:9200

echo "Push mapping to Elasticsearch"

python app/mappingInit.py

echo "Load data to Elasticsearch"

python app/dataLoader.py
