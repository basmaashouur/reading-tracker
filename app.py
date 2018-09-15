# imports
from flask import Flask, render_template, url_for, json
from flask import request, redirect, flash, jsonify, make_response
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker, scoped_session
from model import *
import os, sys
import random
import string
import datetime
import httplib2
import requests


# Flask instance
app = Flask(__name__)

# create engine and enable sharing a session across threads
engine = create_engine('sqlite:///rctrl.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Home page, show all the readings
@app.route('/', methods=['GET'])
@app.route('/home/', methods=['GET'])
def showHome():
     if request.method == 'GET':
        allReadings = session.query(Readings).order_by(desc(Readings.created_at))
        return render_template("home.html", allReadings = allReadings)


# Readings Page, show all the types and it's readings
@app.route('/readings/', methods=['GET', 'POST'])
def showReadings():
    if request.method == 'POST':
        # get the java script var which contains al tags
        #tags =  request.get_json(force=False)
        # format tags because  It comes out as a dictionary
        #tagsFormat = format(tags)
    
        # add all the new tags in the database
        #newtags = Tags(title=request.form['tag'],created_at=datetime.datetime.now())
        #session.add(newtags)

        # add the new readings in the database
        newReadings = Readings(title=request.form['nameR'], img=request.form['img-link'],
         description=request.form['desc'], created_at=datetime.datetime.now())
        session.add(newReadings)

        session.commit()
        return redirect(url_for('showHome'))
    else:
        #sendTags = [r[0] for r in session.query(Tags.title)]
        sendTags =["Science", "Math"]
        return render_template("readings.html", dataPy = json.dumps(sendTags))


# Edit reading
@app.route('/edit/<int:id>/', methods=['GET', 'POST'])
def showToEdit(id):
    editReadings = session.query(Readings).filter_by(id=id).one()
    if request.method == 'POST':
        if request.form['nameR']:
            editReadings.title = request.form['nameR']
        if request.form['desc']:
            editReadings.description = request.form['desc']
        if request.form['img-link']:
            editReadings.img = request.form['img-link']
        session.add(editReadings)
        session.commit()
        return redirect(url_for('showHome'))
    else:
        return render_template("edit.html", id = id, editReadings=editReadings)

# Delete reading
@app.route('/delete/<int:id>/', methods=['GET', 'POST'])
def showToDelete(id):
    deleteReadings = session.query(Readings).filter_by(id=id).one()
    if request.method == 'POST':
        session.delete(deleteReadings)
        session.commit()
        return redirect(url_for('showHome'))
    else:
        #sendTags = [r[0] for r in session.query(Tags.title)]
        sendTags =["Science", "Math"]
        return render_template("delete.html", id = id, deleteReadings=deleteReadings)


# ToRead page, show all the toread 
@app.route('/toread/')
def showToRead():
    return render_template("toread.html")



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)