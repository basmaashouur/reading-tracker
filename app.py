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
        sendTags = [r[0] for r in session.query(Tags.title)]
        #sendTags =["Science", "Math"]
        return render_template("readings.html", dataPy = json.dumps(sendTags))


# Edit reading, id is reading id
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

# Delete reading, id is reading id
@app.route('/delete/<int:id>/', methods=['GET', 'POST'])
def showToDelete(id):
    deleteReadings = session.query(Readings).filter_by(id=id).one()
    if request.method == 'POST':
        if deleteReadings.to_read == True:
            deletetoread = session.query(ToRead).filter_by(readings_id=id).one()
            session.delete(deletetoread)
        session.delete(deleteReadings)
        session.commit()
        return redirect(url_for('showHome'))
    else:
        #sendTags = [r[0] for r in session.query(Tags.title)]
        sendTags =["Science", "Math"]
        return render_template("delete.html", id = id, deleteReadings=deleteReadings)



# Add to read, id is reading id
@app.route('/addtoread/<int:id>/', methods=['GET', 'POST'])
def addToRead(id):
    readings = session.query(Readings).filter_by(id=id).one()
    if request.method == 'POST':
        readings.to_read = True;
        newToRead = ToRead( created_at=datetime.datetime.now(),reading_time = request.form['time'], readings_id = id)
        session.add(newToRead)
        session.add(readings)
        session.commit()
        return redirect(url_for('showToRead'))
    else:
        return render_template("addtoread.html",id = id, readings = readings)



# Show all to read
@app.route('/toread/', methods=['GET', 'POST'])
def showToRead():
    allToRead = session.query(ToRead).order_by(desc(ToRead.created_at))
    allReadings = session.query(Readings)
    return render_template("toread.html", allToRead=allToRead, allReadings=allReadings)

# Show one to read, id is reading id
@app.route('/toread/<int:id>/', methods=['GET', 'POST'])
def showOneToRead(id):
    toRead = session.query(ToRead).filter_by(readings_id=id).one()
    reading = session.query(Readings).filter_by(id=id).one()
    return render_template("onetoread.html", toRead=toRead, reading = reading)


# Edit to read, id is reading id
@app.route('/edittoread/<int:id>/', methods=['GET', 'POST'])
def editToRead(id):
    toRead = session.query(ToRead).filter_by(readings_id=id).one()
    if request.method == 'POST':
        if request.form['time']:
            toRead.reading_time = request.form['time']
        session.add(toRead)
        session.commit()
        return redirect(url_for('showOneToRead', id = id))
    else:
        return render_template("edittoread.html", id = id, toRead=toRead)


# Delete to read
@app.route('/deletetoread/<int:id>/<int:readingid>/', methods=['GET', 'POST'])
def deleteToRead(id, readingid):
    toRead = session.query(ToRead).filter_by(id=id).one()
    editreading = session.query(Readings).filter_by(id=readingid).one()
    if request.method == 'POST':
        editreading.to_read  = False;
        session.add(editreading)
        session.delete(toRead)
        session.commit()
        return redirect(url_for('showHome'))
    else:
        return render_template("deletetoread.html", id = id, readingid=readingid)


@app.route('/check/<int:toreadid>/', methods=['POST'])
def check(toreadid):
    if request.method == 'POST':
        toRead = session.query(ToRead).filter_by(id=toreadid).one()
        toRead.finished = True
        session.add(toRead)
        session.commit()
        return redirect(url_for('showToRead'))





@app.route('/uncheck/<int:toreadid>/', methods=['POST'])
def uncheck(toreadid):
    if request.method == 'POST':
        toRead = session.query(ToRead).filter_by(id=toreadid).one()
        toRead.finished = False
        session.add(toRead)
        session.commit()
        return redirect(url_for('showToRead'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)