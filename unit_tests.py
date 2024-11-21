from main import app

def test_home():
    response = app.test_client().get("/")

    assert response.status_code==200
    assert response.data==b"<h1>Hello Welcome to the Flask app</h1>"