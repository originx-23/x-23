#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import datetime
import subprocess

from flask import send_file
from flask_restful import reqparse, Resource

from cluster.api import api
from universal import x_error
from universal.tables.task import Task_table
from universal.x_jwt import OPERATOR
from universal.x_jwt import allow
parser = reqparse.RequestParser()


class Task(Resource):
    # @allow('Administrator')
    def post(self):
        args = parser.parse_args()
        try:
            start_time = args['start_time']
            dead_time = args['dead_time']
            detail = args['detail']
            participants = args['participants']
            location = args['location']
        except KeyError as e:
            raise x_error.NoParam(e)
        # 添加数据库
        data = Task_table(start_time=start_time, dead_time=dead_time,
                          detail=detail, participants=participants,
                          location=location)
        data.add()

    def delete(self, task_id):
        task_record = Task_table.query.filter(
            Task_table.id == task_id).first()
        if not task_record:
            raise x_error.NotFound('task %s' % task_id)
        task_record.delete()

    def put(self, task_id):
        args = parser.parse_args()
        task_record = Task_table.query.filter(
            Task_table.id == task_id).first()
        task_record.start_time = args['time_stamp']
        task_record.dead_time = args['dead_time']
        task_record.detail = args['detail']
        task_record.participants = args['participants']
        task_record.location = args['location']
        task_record.modify()

    def get(self):
        task_record_list = []
        task_records = Task_table.query.filter().all()
        for task_record in task_records:
            task_record_list.append(
                {'id': task_record.id,
                 'start_time': task_record.start_time,
                 'dead_time': task_record.dead_time,
                 'detail': task_record.detail,
                 'participants': task_record.participants,
                 'location': task_record.location})
        return task_record_list


api.add_resource(Task, "/task",
                 "/task/<string:task_id>")