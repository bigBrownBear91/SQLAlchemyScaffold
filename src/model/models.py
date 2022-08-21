from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class House(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    address = Column(String)
    rooms = relationship("Room", backref='houses')

    def __init__(self, address: str):
        self.address = address


class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    room_type = Column(String)
    house_id = Column(Integer, ForeignKey('houses.id'))

    def __init__(self, room_type: str):
        self.room_type = room_type
