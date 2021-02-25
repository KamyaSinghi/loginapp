#import models
from flask_login import UserMixin
from app import db

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fname = db.Column(db.String(120),  nullable=False)
    lname = db.Column(db.String(120),  nullable=False)
    password = db.Column(db.String(120),  nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username