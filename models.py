import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#회원정보를 만들어보자 - db의 Model을 가져와
class User(db.Model):
    #tablename만들기
    __tablename__ = 'user'

    #column만들기
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32))
    password = db.Column(db.String(64))
    username = db.Column(db.String(8))
