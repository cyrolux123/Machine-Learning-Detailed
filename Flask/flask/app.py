from flask import Flask

'''
It creates an instance of the Flask class, which will be our WSGI(Web Server Gateway Interface) application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask app!"

@app.route("/index")
def index():
    return "Welcome to the index page!"


if __name__ == "__main__":
    app.run(debug=True)