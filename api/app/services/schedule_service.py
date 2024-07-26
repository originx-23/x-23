from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

class ScheduleService:
    def add_schedule(self, user_id, schedule_item):
        doc = {
            'user_id': user_id,
            'item': schedule_item,
            'timestamp': datetime.now(),
        }
        es.index(index='schedule', document=doc)

    def get_schedules(self, user_id):
        res = es.search(index='schedule', body={
            'query': {
                'match': {
                    'user_id': user_id
                }
            }
        })
        return res['hits']['hits']

schedule_service = ScheduleService()
