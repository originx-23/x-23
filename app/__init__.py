from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import home, health, finance, schedule, llama
    app.register_blueprint(home.home_bp)
    app.register_blueprint(health.health_bp)
    app.register_blueprint(finance.finance_bp)
    app.register_blueprint(schedule.schedule_bp)
    app.register_blueprint(llama.llama_bp)
    return app
