from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/auth/register')
def register_user():
    return "Hello, Flask!"

@app.route('/auth/user')
def register_user():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
