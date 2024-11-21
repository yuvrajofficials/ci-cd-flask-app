from src.main import app

def route_test():
    response = app.test_client().get("/")

    assert response.status_code==200
    assert response.data== "<h1>Hello Welcome to the Flask app</h1>"
