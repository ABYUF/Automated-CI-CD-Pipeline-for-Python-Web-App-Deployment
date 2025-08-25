from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Welcome to Automated CI/CD Pipeline for Python Project!"

if __name__ == '__main__':
    app.run()
