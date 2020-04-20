import os

from flask import Flask,session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

from datetime import datetime as dt
from models import users,db


app = Flask(__name__,template_folder='Template')

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key="email"

db.init_app(app)
def main():
    db.create_all()

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register",methods=["GET","POST"])
def register():
    if (request.method == "POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        username = request.form.get("username")
        pwd = request.form.get("password")

        column = users(name = name, email = email, username = username, password = pwd)    
        db.session.add(column)
        db.session.commit()
        a=users.query.all()
        print(a)
        
        # print(request.headers)
        # print(name, email, username, pwd)
        # app.logger.info("name : %s " ,name)
        # app.logger.info("email : %s " ,email)
        # app.logger.info("username : %s " ,username)
        # app.logger.info("password : %s",pwd)
        return render_template("final.html", name=name)

    return render_template("register.html")

@app.route("/admin")
def admin():
    user = users.query.all()
    return render_template("admin.html", user=user)

if __name__ == "__main__":
    with app.app_context():
        main()

    
