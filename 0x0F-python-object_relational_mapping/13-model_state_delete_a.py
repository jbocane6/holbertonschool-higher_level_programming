#!/usr/bin/python3
""" Script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa.
Your script should take 3 arguments:
mysql username, mysql password and database name.
You must use the module SQLAlchemy.
You must import State and Base from model_state -
from model_state import Base, State.
Your script should connect to a MySQL server running on localhost at port 3306.
Your code should not be executed when imported.
"""


from sys import argv
from model_state import State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, password, dbname = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, dbname), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)

    session.commit()
    session.close()
