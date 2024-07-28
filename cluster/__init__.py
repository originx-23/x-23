#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_socketio import SocketIO
from cluster.config import ProdConfig, DevConfig
from universal.request_id import RequestID
from flask_sqlalchemy import SQLAlchemy

# 'eventlet', 'gevent_uwsgi', 'gevent', 'threading'
async_mode = 'threading'     # 新添加的代码
socketio = SocketIO()   # 新添加的代码

if os.getenv("MSW_ENV") == 'prod':
    DefaultConfig = ProdConfig
else:
    DefaultConfig = DevConfig

config = DefaultConfig
app = Flask(__name__)
app.config.from_object(config)


def create_app():
    """Create an application."""
    from .api import api_bp
    app.register_blueprint(api_bp)
    # app初始化必须放在路由注册之后
    RequestID(app)
    socketio.init_app(app=app, async_mode=async_mode)
    return app


db = SQLAlchemy(app)
