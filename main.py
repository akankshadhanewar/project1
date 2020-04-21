import os

from flask import Flask,session,request,render_template,flash,logging,redirect,url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

from datetime import datetime as dt
from models import user,db

app = Flask(__name__,template_folder='Template')

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
