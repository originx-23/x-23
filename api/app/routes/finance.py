from flask import Blueprint, render_template
from api.app.services.finance_service import finance_service

finance_bp = Blueprint('finance', __name__, url_prefix='/finance')

@finance_bp.route('/<user_id>')
def finance(user_id):
    finance_data = finance_service.get_finance_data(user_id)
    return render_template('finance.html', finance_data=finance_data)
