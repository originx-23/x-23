from flask import Blueprint, render_template, request, redirect, url_for
from api.app.services.schedule_service import schedule_service

schedule_bp = Blueprint('schedule', __name__, url_prefix='/schedule')

@schedule_bp.route('/<user_id>')
def schedule(user_id):
    schedules = schedule_service.get_schedules(user_id)
    return render_template('schedule.html', schedules=schedules)

@schedule_bp.route('/', methods=['POST'])
def add_schedule():
    user_id = request.form['user_id']
    schedule_item = request.form['schedule_item']
    schedule_service.add_schedule(user_id, schedule_item)
    return redirect(url_for('schedule.schedule', user_id=user_id))
