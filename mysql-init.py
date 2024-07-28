#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:5220000@127.0.0.1:3306/xover"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class JournalTable(db.Model):
    __tablename__ = 'journal'
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.String(32), nullable=False)
    data = db.Column(db.String(233), nullable=False)
    location = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Journal %r>' % self.id


db.drop_all()
db.create_all()
date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
u = JournalTable(location='root',
                 data='feffcb602a3c77e7354e9d1c7ceef603',
                 time_stamp=date)
db.session.add(u)
db.session.commit()
