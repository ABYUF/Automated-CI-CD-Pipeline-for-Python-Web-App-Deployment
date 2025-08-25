from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, Welcome to Automated CI/CD Pipeline for Python Project!" in response.data
