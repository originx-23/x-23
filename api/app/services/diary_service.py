from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

class DiaryService:
    def add_diary(self, user_id, diary_entry):
        doc = {
            'user_id': user_id,
            'entry': diary_entry,
            'timestamp': datetime.now(),
        }
        es.index(index='diary', document=doc)

    def get_diaries(self, user_id):
        res = es.search(index='diary', body={
            'query': {
                'match': {
                    'user_id': user_id
                }
            }
        })
        return res['hits']['hits']

diary_service = DiaryService()
