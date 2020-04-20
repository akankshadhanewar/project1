import os
from datetime import datetime
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class users(db.Model):
    __tablename__ = "users"
    name = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=False, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    def __init__(self,name,email,username,password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.time = datetime.now()
