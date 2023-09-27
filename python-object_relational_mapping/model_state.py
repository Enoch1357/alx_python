#! /usr/bin/python3
"""
This module contains a class definition of a state;
'declarative_base()'
"""
import sqlalchemy
Base = declarative_base()

class State(Base):
    """This is a class State that inherits from the class Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
