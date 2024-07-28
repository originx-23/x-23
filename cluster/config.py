#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import os


class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    ERROR_404_HELP = False


class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    # todo: 明确配置信息
    # 配置MySQL的uri的格式为: mysql://username:password@hostname/database
    SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://root:5220000"
                               "@127.0.0.1:3306/xover")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    # todo: 明确配置信息
    # 配置MySQL的uri的格式为: mysql://username:password@hostname/database
    SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://root:5220000"
                               "@127.0.0.1:3306/xover")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
