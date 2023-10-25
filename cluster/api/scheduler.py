#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import datetime
import subprocess

from flask import send_file
from flask_restful import reqparse, Resource

from cluster.api import api
from universal import x_error
from universal.tables.schedule import ScheduleTable
from universal.x_jwt import OPERATOR
from universal.x_jwt import allow
parser = reqparse.RequestParser()


class Scheduler(Resource):
    # @allow('Administrator')
    def post(self):
        args = parser.parse_args()
        try:
            start_time = args['start_time']
            end_time = args['end_time']
            detail = args['detail']
            participants = args['participants']
            location = args['location']
        except KeyError as e:
            raise x_error.NoParam(e)
        # 添加数据库
        data = ScheduleTable(start_time=start_time, end_time=end_time,
                             detail=detail, participants=participants,
                             location=location)
        data.add()

    def delete(self, schedule_id):
        schedule_record = ScheduleTable.query.filter(
            ScheduleTable.id == schedule_id).first()
        if not schedule_record:
            raise x_error.NotFound('schedule %s' % schedule_id)
        schedule_record.delete()

    def put(self, schedule_id):
        args = parser.parse_args()
        schedule_record = ScheduleTable.query.filter(
            ScheduleTable.id == schedule_id).first()
        schedule_record.start_time = args['time_stamp']
        schedule_record.end_time = args['end_time']
        schedule_record.detail = args['detail']
        schedule_record.participants = args['participants']
        schedule_record.location = args['location']
        schedule_record.modify()

    def get(self):
        schedule_record_list = []
        schedule_records = ScheduleTable.query.filter().all()
        for schedule_record in schedule_records:
            schedule_record_list.append(
                {'id': schedule_record.id,
                 'start_time': schedule_record.start_time,
                 'end_time': schedule_record.end_time,
                 'detail': schedule_record.detail,
                 'participants': schedule_record.participants,
                 'location': schedule_record.location})
        return schedule_record_list


api.add_resource(Scheduler, "/schedule",
                 "/schedule/<string:schedule_id>")
