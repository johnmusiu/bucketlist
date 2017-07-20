#imports sys module: can be used to manipulate runtime en
import sys
from sqlalchemy import *
#for use in mapper code
from sqlalchemy import Column, ForeignKey, Integer, String
#use in config and class code
from sqlalchemy.ext.declarative import declarative_base
#for foreign key creation
from sqlalchemy.orm import relationship
#for use in mapper
from sqlalchemy import create_engine

engine = create_engine('sqlite:///bucketlist.db', echo = True)

#shows our classes are special alchemy classes that correspond to tables in our database
Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	username = Column(String(20), nullable = False)
	email = Column(String(30), nullable = False)
	password = Column(String(30), nullable = False)

	def __init__(self, id, name, username, email, password):
		self.id = id
		self.name =name
		self.username = username
		self.email = email
		self.password = password


class Bucketlist(Base):
	__tablename__ = 'bucketlists'
	id = Column(Integer, primary_key = True)
	title = Column(String(80), nullable = False)
	description = Column(String(254), nullable = False)
	user_id = Column(Integer, ForeignKey('users.id'))

	user = relationship(User)
	def __init__(self, id, title, description, user_id):
		self.id = id
		self.title = title
		self.description = description
		self.user_id = user_id
class Activities(Base):
	__tablename__ = 'activities'
	id = Column(Integer, primary_key = True)
	title = Column(String(80), nullable = False)
	description = Column(String(254), nullable = False)
	place = Column(String(50))
	people = Column(String(254))
	bucketlist_id = Column(Integer, ForeignKey('bucketlists.id'))

	bucketlist = relationship(Bucketlist)

	def __init__(self, id, title, description, place, people, bucketlist_id):
		self.id = id
		self.title = title
		self.description = description
		self.place = place
		self.people = people
		self.bucketlist_id = bucketlist_id

#add to bottom
#adds classes as tables to database
Base.metadata.create_all(engine)