from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')

@home_bp.route('/plan', methods=['POST'])
def plan():
    user_input = request.form.get('user_input')
    response = llama_service.get_inference(user_input)
    return render_template('result.html', response=response)
