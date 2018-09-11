# imports
from flask import Flask, render_template, url_for, json
from flask import request, redirect, flash, jsonify, make_response
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from model import *
import os
import random
import string
import datetime
import httplib2
import requests


# Flask instance
app = Flask(__name__)

engine = create_engine('sqlite:///rctrl.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Home page, show the latest readings
@app.route('/', methods=['GET'])
@app.route('/home/', methods=['GET'])
def showHome():
    return render_template("home.html")


# Readings Page, show all the types and it's readings
@app.route('/readings/', methods=['GET', 'POST'])
def showReadings():
    if request.method == 'POST':
        newreadings = Readings(title=request.form['name'], img=request.form['img-link'],
         description=request.form['desc'], created_at=datetime.datetime.now())
        newtag = Tags(title=request.form['tag'],created_at=datetime.datetime.now())
        session.add(newreadings)
        session.add(newtag)
        session.commit()
        return redirect(url_for('showHome'))
    else:
        alltags = session.query(Tags.title)
        data = ["basma", "ashour","zomrawy","ali"]
        return render_template("readings.html", dataPy = json.dumps(alltags))


# ToRead page, show all the toread 
@app.route('/toread/')
def showToRead():
    return render_template("toread.html")



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)