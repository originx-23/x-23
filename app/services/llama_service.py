import requests

class LlamaService:
    def __init__(self, inference_url):
        self.inference_url = inference_url

    def get_inference(self, prompt):
        response = requests.post(self.inference_url, json={"prompt": prompt})
        return response.json()

llama_service = LlamaService('http://localhost:5000/inference')

