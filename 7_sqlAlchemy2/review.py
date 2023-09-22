# Imports
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

#initialize with decrative base
Base = declarative_base()

#Creating a class that works with a table (child component of the base)
#Create tables
    #Create the engine
    #Create the tables based on out parent base


# Delete all our tables and remake them


# Add a object
    # Create the engine
    # Create a session from that engine (Allowing us to create tables)
        # Using .add we can now add an object
        # Make sure to commit

#Get all data

# Filter

#Update

#With a delete we need to first query!

if __name__ == '__main__':
        
    pass