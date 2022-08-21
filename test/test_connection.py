import pytest

from src.model.session import Session
from src.model.models import House
from test.fixtures import create_session


def test_connection(create_session):
    house = House('Testaddress 1')
    session = create_session()
    session.create(house)

    new_session = create_session()
    fetched_house = new_session.get_by_id(House, 1)
    assert house != fetched_house
    assert fetched_house.address == 'Testaddress 1'
