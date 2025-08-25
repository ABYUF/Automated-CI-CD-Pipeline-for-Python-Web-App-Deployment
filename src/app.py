from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h2>Hello, Welcome to Automated CI/CD Pipeline for Python Project!</h2>
    <p>Flask, Gunicorn, Nginx, Flake8 is successfully installed and working!</p>
    <p>Successfully "BUILD & DEPLOYED PYTHON WEB APPLICATION ON EC2 USING GitHub Actions Workflow", Integrated with Linting and Unti Testing!</p>
    """

if __name__ == '__main__':
    app.run()
