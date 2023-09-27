#! /usr/bin/python3
"""
This module lists all 'Stat' objects from the database hbtn_0e_6_usa
"""
import sqlalchemy
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
states = session.query(State).order_by(State.id).all()
for state in states:
    print(f"{state.id}: {state.name}")
session.close()
