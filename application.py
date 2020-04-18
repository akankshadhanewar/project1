import os
from flask import Flask, render_template,request
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__,template_folder='Template')

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# # Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = True
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template ("home.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if (request.method == "POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        username = request.form.get("username")
        pwd = request.form.get("password")    
        # print(request.headers)
        # print(name, email, username, pwd)
        app.logger.info("name : %s " ,name)
        app.logger.info("email : %s " ,email)
        app.logger.info("username : %s " ,username)
        app.logger.info("password : %s",pwd)
        name=name.capitalize() 
        return render_template("login.html", name=name)

    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if (request.method == "POST"):
        username = request.form.get("username")
        pwd = request.form.get("password")
        # print(request.headers)
        app.logger.info("username : %s" ,username)
        app.logger.info("password : %s",pwd)
        username=username.capitalize()
        return render_template("final.html",name=username)

    return render_template("login.html")