import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Tags(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=True)


class Readings(Base):
    __tablename__ = 'readings'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    img = Column(String(400), nullable=True)
    description = Column(String(600), nullable=True)
    created_at = Column(DateTime, nullable=True)
    to_read = Column(Boolean, unique=False, default=False)


class ReadingsTags(Base):
    __tablename__ = 'readingsTags'

    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer)
    readings_id = Column(Integer)

    
class ToRead(Base):
    __tablename__ = 'toRead'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    reading_time = Column(Integer)
    finished = Column(Boolean, unique=False, default=False)
    readings_id = Column(Integer, ForeignKey('readings.id'))
    readings = relationship(Readings, backref="toRead")

engine = create_engine('sqlite:///rctrl.db')


Base.metadata.create_all(engine)
