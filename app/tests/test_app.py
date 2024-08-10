import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test the homepage."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Brewery Finder App' in response.data

def test_get_breweries(client):
    """Test the brewery search with state parameter."""
    response = client.post('/get_breweries', data={'state': 'california'})
    assert response.status_code == 200
    assert b'10 Barrel Brewing Co' in response.data
    #When testing the API pull from california, 10 Barrel Brewing Co is the first one.
    #If we see this string then we know the test was successful
