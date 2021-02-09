

import pytest

from startup import create_app

@pytest.fixture
def client():
    return create_app("test").test_client()

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/api/1.0/stock/test')

    print(rv.data)
    assert b'{"error": "Not found"}' in rv.data

