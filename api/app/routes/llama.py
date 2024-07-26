from flask import Blueprint, render_template, request
from api.app.services.llama_service import llama_service
from api.app.services.schedule_service import schedule_service
from api.app.services.diary_service import diary_service

llama_bp = Blueprint('llama', __name__, url_prefix='/llama')


@llama_bp.route('/', methods=['POST'])
def get_inference():
    prompt = request.form['prompt']
    user_id = request.form['user_id']
    response = llama_service.get_inference(prompt)

    # 分析响应以决定是日记还是日程
    if "schedule" in response:
        schedule_item = response["schedule"]
        schedule_service.add_schedule(user_id, schedule_item)
    elif "diary" in response:
        diary_entry = response["diary"]
        diary_service.add_diary(user_id, diary_entry)

    return render_template('result.html', response=response)
