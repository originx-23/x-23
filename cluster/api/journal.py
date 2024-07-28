#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import datetime
import subprocess

from flask import send_file
from flask_restful import reqparse, Resource

from cluster.api import api
from universal import x_error
from universal.tables.journal import JournalTable
from universal.x_jwt import OPERATOR
from universal.x_jwt import allow
parser = reqparse.RequestParser()


class JournalRecord(Resource):
    @allow('Administrator')
    def post(self):
        args = parser.parse_args()
        try:
            time_stamp = args['time_stamp']
            detail = args['detail']
            location = args['location']
        except KeyError as e:
            raise x_error.NoParam(e)
        # 添加数据库
        data = JournalTable(time_stamp=time_stamp, detail=detail,
                            location=location)
        data.add()

    def delete(self, jr_id):
        journal_record = JournalTable.query.filter(
            JournalTable.id == jr_id).first()
        if not journal_record:
            raise x_error.NotFound('journal %s' % jr_id)
        journal_record.delete()

    def put(self, jr_id):
        args = parser.parse_args()
        journal_record = JournalTable.query.filter(
            JournalTable.id == jr_id).first()
        journal_record.time_stamp = args['time_stamp']
        journal_record.data = args['detail']
        journal_record.location = args['location']
        journal_record.modify()

    def get(self):
        journal_record_list = []
        journal_records = JournalTable.query.filter().all()
        for journal_record in journal_records:
            journal_record_list.append(
                {'id': journal_record.id,
                 'time_stamp': journal_record.time_stamp,
                 'detail': journal_record.detail,
                 'location': journal_record.location})
        return journal_record_list

    def journal_in(self):
        pass
        # todo 写入日志中

    def journal_out(self):
        pass
        # TODO 从日志写入文件，生成日记


api.add_resource(JournalRecord, "/journal_record",
                 "/journal_record/<string:jr_id>")