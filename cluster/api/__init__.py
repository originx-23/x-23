#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import jsonify
from flask_restful import Api
from universal.x_jwt import create_token, get_host_ip
from universal import x_error
import socket

# 生成g_token
ipaddr = get_host_ip()
g_token = create_token("Administrator", "cluster_api", ipaddr, 99999)

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(api_bp)


@api_bp.errorhandler(x_error.Error)
def handle_error(err):
    response = jsonify(err.to_dict())
    response.status_code = err.code
    return response


from . import journal
from . import scheduler
from . import skill

