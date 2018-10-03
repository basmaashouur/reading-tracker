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

# create engine and enable sharing a session across threads
engine = create_engine('sqlite:///rctrl.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# add tags
tag1 = Tags(title='science',created_at=datetime.datetime.now())
session.add(tag1)

tag2 = Tags(title='math',created_at=datetime.datetime.now())
session.add(tag2)

tag3 = Tags(title='bio',created_at=datetime.datetime.now())
session.add(tag3)

tag4 = Tags(title='cs',created_at=datetime.datetime.now())
session.add(tag4)

tag5 = Tags(title='history',created_at=datetime.datetime.now())
session.add(tag5)

tag6 = Tags(title='english',created_at=datetime.datetime.now())
session.add(tag6)

tag7 = Tags(title='french',created_at=datetime.datetime.now())
session.add(tag7)

tag8 = Tags(title='cosmo',created_at=datetime.datetime.now())
session.add(tag8)

tag9 = Tags(title='poet',created_at=datetime.datetime.now())
session.add(tag9)

tag10 = Tags(title='art',created_at=datetime.datetime.now())
session.add(tag10)

tag11 = Tags(title='AI',created_at=datetime.datetime.now())
session.add(tag11)

tag12 = Tags(title='ML',created_at=datetime.datetime.now())
session.add(tag12)

tag13 = Tags(title='Algorithms',created_at=datetime.datetime.now())
session.add(tag13)

tag14 = Tags(title='design',created_at=datetime.datetime.now())
session.add(tag14)

tag15 = Tags(title='network',created_at=datetime.datetime.now())
session.add(tag15)

tag16 = Tags(title='security',created_at=datetime.datetime.now())
session.add(tag16)


# add readings


reading1 = Readings(title='book1', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading1)

reading2 = Readings(title='book2', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading2)

reading3 = Readings(title='book3', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading3)

reading4 = Readings(title='book4', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading4)

reading5 = Readings(title='book5', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading5)

reading6 = Readings(title='book6', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading6)

reading7 = Readings(title='book7', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading7)

reading8 = Readings(title='book8', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading8)

reading9 = Readings(title='book9', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading9)

reading10 = Readings(title='book10', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading10)

reading11 = Readings(title='book11', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading11)

reading12 = Readings(title='book12', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading12)

reading13 = Readings(title='book13', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading13)

reading14 = Readings(title='book14', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading14)

reading15 = Readings(title='book15', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading15)

reading16 = Readings(title='book16', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading16)

reading17 = Readings(title='book17', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading17)

reading18 = Readings(title='book18', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading18)

reading19 = Readings(title='book19', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading19)

reading20 = Readings(title='book20', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading20)

reading21 = Readings(title='book21', img='', description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', created_at=datetime.datetime.now())
session.add(reading21)






session.commit()
print ("Your database has been populated with fake data!")