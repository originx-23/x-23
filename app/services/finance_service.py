import requests

class FinanceService:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_finance_data(self, user_id):
        response = requests.get(f'https://api.finance.com/users/{user_id}/data', headers={'Authorization': f'Bearer {self.api_key}'})
        return response.json()

finance_service = FinanceService('your_api_key_here')

