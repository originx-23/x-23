from flask import Blueprint, render_template
from app.services.health_service import health_service

health_bp = Blueprint('health', __name__, url_prefix='/health')

@health_bp.route('/<user_id>')
def health(user_id):
    health_data = health_service.get_health_data(user_id)
    return render_template('health.html', health_data=health_data)
