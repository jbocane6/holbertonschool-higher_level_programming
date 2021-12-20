#!/usr/bin/python3
""" Python file that contains the class definition of a State
and an instance Base = declarative_base():
State class:
inherits from Base Tips.
links to the MySQL table states.
class attribute id that represents a column of an auto-generated,
unique integer, can’t be null and is a primary key.
class attribute name that represents a column of a string
with maximum 128 characters and can’t be null.
You must use the module SQLAlchemy.
Your script should connect to a MySQL server running on localhost at port 3306.
WARNING: all classes who inherit from Base must be imported
before calling Base.metadata.create_all(engine).
"""


import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
