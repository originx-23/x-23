class HealthService:
    def __init__(self):
        pass

    def get_health_data(self, user_id):
        # 模拟数据
        health_data = {
            "steps": 10000,
            "heart_rate": 70,
            "sleep_hours": 8,
            "calories_burned": 500
        }
        return health_data

health_service = HealthService()
