import os

from flask import Flask,session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

from datetime import datetime as dt
from models import user,db


app = Flask(__name__,template_folder='Template')

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key="email"

db.init_app(app)

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
        email = request.form.get("email")
        pwd = request.form.get("password")

        mail = user.query.filter_by(email=email)
        print(mail)
        try:
            row = user(email = email, password = pwd)    
            db.session.add(row)
            db.session.commit()
            return render_template("register.html",email=email)
        except:
            error_msg = "Email already exist"
            return render_template("register.html", msg = error_msg)
    return render_template("register.html")

@app.route("/admin")
def admin():
    user_data = user.query.all()
    return render_template("admin.html", user=user_data)

@app.route("/auth", methods=["GET","POST"])
def auth():
    if (request.method == "POST"):
        email = request.form.get("email")
        pwd = request.form.get("password")
        u_mail = user.query.get(email)
        if u_mail != None:

            if pwd == u_mail.password:
                session["email"] = email
                return render_template("home.html")
            else:
                e_msg = "Please check the password"
                return render_template("register.html",p_msg=e_msg)
        else:
            e_msg = "You have not yet registered"
            return render_template("register.html",msg=e_msg)

@app.route("/logout")
def logout():
    session["email"]=None
    return redirect("/register")


    
