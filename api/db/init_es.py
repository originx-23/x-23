from elasticsearch import Elasticsearch
import yaml
import os


def load_es_config():
    with open(os.path.join(os.path.dirname(__file__), '../../conf/es_config.yaml'), 'r') as file:
        config = yaml.safe_load(file)
    return config


def init_es():
    config = load_es_config()
    es = Elasticsearch(
        config['es']['hosts'],
        http_auth=(config['es']['username'], config['es']['password'])
    )
    return es


if __name__ == "__main__":
    es = init_es()
    if es.ping():
        print("Elasticsearch connected successfully!")
    else:
        print("Failed to connect to Elasticsearch.")
