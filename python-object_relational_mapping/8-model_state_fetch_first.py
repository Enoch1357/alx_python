#! /usr/bin/pytohn3
"""
This module  prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
engine = create_engine(f"mysql+mysqldb://{username}:{password}\
                       @localhost:3306/{database_name}")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
first_state = session.query(State).order_by(State.id).first()
if first_state is None:
    print("Nothing", end="\n")
else:
    print(f"{first_state.id}: {first_state.name}")
session.close()
