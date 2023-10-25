#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from sqlalchemy import exc

from cluster import db
from universal import x_error


class AttributeTable(db.Model):
    __tablename__ = 'attribute'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    iq = db.Column(db.Integer, nullable=False)
    # 名字
    names = db.Column(db.JSON, nullable=False)
    # 心理指标
    mentality = db.Column(db.JSON, nullable=False)
    # 面部评价
    appearance = db.Column(db.JSON, nullable=False)
    # 外部声誉(领域-声誉)
    reputation = db.Column(db.JSON, nullable=False)
    # 身体力量属性
    strength = db.Column(db.JSON, nullable=False)
    # 财富
    property = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return '<Attribute %r>' % self.id

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            raise x_error.ServiceError('Failed to add attribute record.')
        return self

    def modify(self):
        try:
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            raise x_error.ServiceError('Failed to modify attribute record.')
        return self

    def delete(self):
        try:
            db.session.delete(self)
        except exc.IntegrityError:
            db.session.rollback()
            raise x_error.ServiceError('Failed to delete attribute record.')
