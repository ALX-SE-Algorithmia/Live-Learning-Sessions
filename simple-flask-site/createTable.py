# This Python Script helps us to create
# a database table in MySQL using SQLAlchemy
#
# Helping with the import and use of
# environmental variables in this directory
import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


# Load the environmental variables from my .env file
load_dotenv()

# Storing the database url I saved as an
# environmental variable (in the .env file)
# to a string
myDbURL = os.getenv('SQLALCHEMY_DATABASE_URI')

Base = declarative_base()  # An instance of the declarative_base class


class User(Base):
    """
    A class that creates a User table in the remote database

    Attributes:
        userId: The user's unique ID
        firstname: User's first name
        lastname: User's last name
        email: User's email address
        password: User's password
    """
    __tablename__ = 'users'  # The table name in the remote database
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    userId = Column(Integer, primary_key=True, autoincrement=True)

# Using a 'try - except' block to
# attempt the connection to the
# database using Python ORM and
# creating a table
try:
    engine = create_engine(myDbURL, echo=True)
    Base.metadata.create_all(engine)
    print("Connection Successful And Table Created Successfully!")
except:
    print("Connection failed, and table not created")
