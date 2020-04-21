import os
from datetime import datetime
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class user(db.Model):
    __tablename__ = "user"
    email = db.Column(db.String(40), nullable=False, primary_key=True)
    password = db.Column(db.String(40), nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.time = datetime.now()
