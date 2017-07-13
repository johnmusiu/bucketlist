import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *
	 
engine = create_engine('sqlite:///bucketlist.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User(1, "admin admin", "admin", "admin@localhost", "password")
session.add(user)
 
user = User(2, "python major", "python","admin@python", "python")
session.add(user)
 
 
# commit the record the database
session.commit()
 
session.commit()