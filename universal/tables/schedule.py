#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from sqlalchemy import exc

from cluster import db
from universal import x_error


class ScheduleTable(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.TIMESTAMP, nullable=False)
    end_time = db.Column(db.TIMESTAMP, nullable=False)
    detail = db.Column(db.Text(233), nullable=False)
    # todo: 参与人员--关联人际表
    participants = db.Column(db.String(233), nullable=False)
    location = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Schedule %r>' % self.id

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            raise x_error.ServiceError('Failed to add schedule record.')
        return self

    def modify(self):
        try:
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            raise x_error.ServiceError('Failed to modify schedule record.')
        return self

    def delete(self):
        try:
            db.session.delete(self)
        except exc.IntegrityError:
            db.session.rollback()
            raise x_error.ServiceError('Failed to delete schedule record.')
