import pytest

from src.model.models import House, Room
from test.fixtures import create_session


def test_relationship_house_to_room(create_session):
    house = House('Teststrasse 1')
    room = Room('Wohnzimmer')
    house.rooms.append(room)

    session = create_session()
    session.create(house)
    session.create(room)

    new_session = create_session()
    fetched_house = new_session.get_by_id(House, 1)
    fetched_room = new_session.get_by_id(Room, 1)

    assert fetched_house.address == 'Teststrasse 1'
    assert fetched_house.rooms[0] == fetched_room
    assert fetched_room.room_type == 'Wohnzimmer'
