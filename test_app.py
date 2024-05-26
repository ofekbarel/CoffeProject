import time
import pytest
from app import app, db, User, PublicRecipe, PrivetRecipe
from app import current_user

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/users'  # Using a separate test database
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()



def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_login(client):
    response = client.post('/login', data={'email': 'test@example.com', 'password': 'password'})
    assert response.status_code < 400


def test_register(client):
    response = client.post('/register', data={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
    assert response.status_code < 400

    user = db.session.query(User).filter(User.email == 'test@example.com').first()

    assert user is not None
    assert response.content_type == 'text/html; charset=utf-8'


    db.session.delete(user)
    db.session.commit()
    db.session.remove()



def test_dashboard(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code < 400
    assert response.content_type == 'text/html; charset=utf-8'





def test_add_public_recipe(client):
    client.post('/register', data={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
    client.post('/login', data={'email': 'test@example.com', 'password': 'password'})
    response = client.post('/add_public_recipe', data={'title': 'Test Public Recipe', 'description': 'This is a test public recipe'})

    assert response.status_code < 400
    recipe = PublicRecipe.query.filter_by(title='Test Public Recipe').first()
    assert recipe is not None
    assert response.content_type == 'text/html; charset=utf-8'

    # Clean up: delete the added recipe
    user = db.session.query(User).filter(User.email == 'test@example.com').first()
    db.session.delete(recipe)
    db.session.delete(user)
    db.session.commit()




def test_add_privet_recipe(client):
    client.post('/register', data={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
    client.post('/login', data={'email': 'test@example.com', 'password': 'password'})
    response = client.post('/add_privet_recipe', data={'title': 'Test Public Recipe', 'description': 'This is a test public recipe'})


    assert response.status_code < 400
    recipe = PrivetRecipe.query.filter_by(title='Test Public Recipe').first()
    assert recipe is not None
    assert response.content_type == 'text/html; charset=utf-8'


    # Clean up: delete the added recipe
    user = db.session.query(User).filter(User.email == 'test@example.com').first()
    db.session.delete(recipe)
    db.session.delete(user)
    db.session.commit()




def test_gallery(client):
    # Simulate a GET request to fetch the gallery page
    response = client.get('/gallery')

    # Check if the response status code is OK
    assert response.status_code == 200
    # Check if the response is of type 'text/html'
    assert response.content_type == 'text/html; charset=utf-8'



def test_random_recipe(client):
    # Simulate a GET request to fetch a random recipe
    response = client.get('/random_recipe')

    # Check if the response status code is OK
    assert response.status_code == 200










