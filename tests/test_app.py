from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

    expected_html = """
    <h2>Hello, Welcome to Automated CI/CD Pipeline for Python Project!</h2>
    <p>Flask, Gunicorn, Nginx, Flake8 is successfully installed and working!</p>
    <p>Successfully "BUILD & DEPLOYED PYTHON WEB APPLICATION ON EC2 USING GitHub Actions Workflow", Integrated with Linting and Unti Testing!</p>
    """

    assert expected_html.strip() in response.data.decode()
