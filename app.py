#This is the main page for the flask code
from flask import Flask
app = Flask(__name__)
@app.route("/welcome")
def welcome():
    return "Welcome to the page!!"

if __name__ = "__main__":
    app.run(debug=True)
