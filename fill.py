import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# create engine and enable sharing a session across threads
engine = create_engine('sqlite:///rctrl.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

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
