import requests


class LlamaService:
    def __init__(self, inference_url):
        self.inference_url = inference_url

    def get_inference(self, prompt):
        response = requests.post(self.inference_url, json={"prompt": prompt})
        result = response.json()

        # 解析响应，返回结构化数据
        if "add schedule" in result:
            schedule_item = self.parse_schedule(result["text"])
            return {"schedule": schedule_item}
        elif "add diary" in result:
            diary_entry = self.parse_diary(result["text"])
            return {"diary": diary_entry}
        else:
            return {"text": result["text"]}

    def parse_schedule(self, text):
        # 根据实际需要实现解析逻辑
        return text.split("schedule:")[1].strip()

    def parse_diary(self, text):
        # 根据实际需要实现解析逻辑
        return text.split("diary:")[1].strip()


llama_service = LlamaService('http://localhost:5000/inference')
