from flask import Blueprint, render_template, request
from app.services.llama_service import llama_service

llama_bp = Blueprint('llama', __name__, url_prefix='/llama')


@llama_bp.route('/', methods=['POST'])
def get_inference():
    prompt = request.form['prompt']
    response = llama_service.get_inference(prompt)
    return render_template('result.html', response=response)
