#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import datetime
import socket

import jwt
from flask import request
from jwt import PyJWTError
from universal import x_error
from universal import httpstatus

screct_key = "screct"
role_map = ["Auditor", "Operator", "Administrator"]
ADMIN = "Administrator"
OPERATOR = "Operator"
AUDITOR = "Auditor"


def get_host_ip():
    # 查询本机ip地址
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except socket.error:
        return 'Unknown'


def create_token(role, user_name, ip, day=15):
    # 构造header
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'}
    # 构造payload
    payload = {
        'role': role,
        'ip': ip,
        'user_name': user_name,
        'exp': datetime.datetime.now() + datetime.timedelta(days=day)
        }

    token = jwt.encode(payload=payload, key=screct_key, algorithm='HS256',
                       headers=headers)
    return token


def allow(role):
    def check(f):
        def _check_token(*args, **kwargs):
            try:
                if "Authorization" not in request.headers:
                    raise x_error.Unauthorized("jwt check failed: no jwt")
                token = request.headers.get('Authorization')
                data = jwt.decode(token, key=screct_key, algorithms='HS256')

                hostname = socket.getfqdn(socket.gethostname())
                ipaddr = socket.gethostbyname(hostname)
                # 判断ip是否符合
                if data['ip'] != str(request.remote_addr):
                    if (data['ip'] == "127.0.0.1") and (
                            str(request.remote_addr) != ipaddr):
                        raise x_error.Unauthorized(
                            "jwt check failed: error ip")
                # 非法的role
                if data['role'] not in role_map:
                    raise x_error.Unauthorized("jwt check failed: error "
                                               "role: %s" % data['role'])
                # 判断是否有权限
                if role_map.index(data['role']) < role_map.index(role):
                    raise x_error.Unauthorized("jwt check failed: role not "
                                               "allow")
                return f(*args, **kwargs)
            except PyJWTError as e:
                raise x_error.Unauthorized("jwt check failed: %s" % e)
        return _check_token
    return check
