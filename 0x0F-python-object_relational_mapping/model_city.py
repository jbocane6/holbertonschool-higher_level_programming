#!/usr/bin/python3
"""Class City representing the table 'cities' on MySQL with id, name
and state_id."""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Basic City mapping with id and name and state_id"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
