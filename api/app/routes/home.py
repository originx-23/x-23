from flask import Blueprint, render_template, request
from api.app.services.llama_service import llama_service
from api.app.services.health_service import health_service
from api.app.services.finance_service import finance_service
from api.app.services.schedule_service import schedule_service

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')

@home_bp.route('/plan', methods=['POST'])
def plan():
    user_input = request.form.get('user_input')
    response = llama_service.get_inference(user_input)
    return render_template('result.html', response=response)

@home_bp.route('/health')
def health():
    user_id = request.args.get('user_id')
    health_data = health_service.get_health_data(user_id)
    return render_template('health.html', health_data=health_data)

@home_bp.route('/finance')
def finance():
    user_id = request.args.get('user_id')
    finance_data = finance_service.get_finance_data(user_id)
    return render_template('finance.html', finance_data=finance_data)

@home_bp.route('/schedule', methods=['POST'])
def schedule():
    user_id = request.form.get('user_id')
    schedule_item = request.form.get('schedule_item')
    schedule_service.add_schedule(user_id, schedule_item)
    schedules = schedule_service.get_schedules(user_id)
    return render_template('schedule.html', schedules=schedules)
