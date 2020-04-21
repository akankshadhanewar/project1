import os
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
import csv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://fgmmfujhuzbzcs:58c9434f1952e27a688611cbafedbb6d2f42acadf9ee7e06aa8531c825d1dc1f@ec2-52-202-146-43.compute-1.amazonaws.com:5432/d9mmenhmerhm08"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Books(db.Model):
    __tablename__="books"
    isbn=db.Column(db.String,primary_key=True)
    title=db.Column(db.String,nullable=False)
    author=db.Column(db.String,nullable=False)
    year=db.Column(db.String,nullable=False)

    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

def main():
    db.create_all()
    book_file = open("books.csv")
    row = csv.reader(book_file)
    for isbn,title,author,year in row:
        book = Books(isbn=isbn, title=title, author=author, year=year)
        db.session.add(book)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()