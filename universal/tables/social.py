#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from sqlalchemy import exc

from cluster import db
from universal import x_error


class SocialTable(db.Model):
    __tablename__ = 'social'
    id = db.Column(db.Integer, primary_key=True)
    # 名字
    name = db.Column(db.String(233), nullable=False)
    # 好感度
    favorability = db.Column(db.Integer, nullable=False)
    # 联系方式, 更多联系方式微博 等等,可以自定义添加
    contact_information = db.Column(db.JSON, nullable=True)
    # 生日
    birthday = db.Column(db.TIMESTAMP, nullable=False)
    # 关系
    role = db.Column(db.JSON, nullable=True)
    # 交往事件(期望这里出现的是日志的ID)
    # 在傻妞的记忆里，您在某年某月与某某发生了某某事
    history = db.Column(db.text)

    def __repr__(self):
        return '<Social %r>' % self.id

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            raise x_error.ServiceError('Failed to add social record.')
        return self

    def modify(self):
        try:
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            raise x_error.ServiceError('Failed to modify social record.')
        return self

    def delete(self):
        try:
            db.session.delete(self)
        except exc.IntegrityError:
            db.session.rollback()
            raise x_error.ServiceError('Failed to delete social record.')
