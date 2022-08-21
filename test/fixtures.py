import os

import pytest

from src.model.session import Session


@pytest.fixture(autouse=True)
def create_session():
    # Fixture returns a function to create a session if more than one session is needed in a test
    def get_session():
        return Session()

    yield get_session
    if os.path.exists('test.db'):
        os.remove('test.db')
