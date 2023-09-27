#! /usr/bin/python3
"""
This module lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
engine = create_engine(f"mysql+mysqldb://{username}:{password}\
                       @localhost:3306/{database_name}")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
states_with_a = session.query(State).filter(
                                            State.name.like('%a%')).order_by(State.id).all()
for state in states_with_a:
    print(f"{state.id}: {state.name}")
session.close()
