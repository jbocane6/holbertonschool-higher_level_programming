#!/usr/bin/python3
""" Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Your script should take 4 arguments:
mysql username, mysql password, database name and state name
to search (SQL injection free).
You must use the module SQLAlchemy.
You must import State and Base from model_state -
from model_state import Base, State.
Your script should connect to a MySQL server running on localhost at port 3306.
You can assume you have one record with the state name to search.
Results must display the states.id.
If no state has the name you searched for, display Not found.
Your code should not be executed when imported.
"""


from sys import argv
from model_state import State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, password, dbname, query = argv[1], argv[2], argv[3], argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, dbname), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id).filter(State.name == query).\
        order_by(State.id).first()
    if state:
        print("{:d}".format(state.id))
    else:
        print("Not found")

    session.close()
