import requests

class HealthService:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_health_data(self, user_id):
        response = requests.get(f'https://api.health.com/users/{user_id}/data', headers={'Authorization': f'Bearer {self.api_key}'})
        return response.json()

health_service = HealthService('your_api_key_here')

