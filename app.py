from flask import Flask

app = Flask(__name__)
from markupsafe import escape

@app.route("/")
def  helloWorld():
     print ("hello bro")
     return f'https://render-flask-8xdc.onrender.com/name'
     print ("hii bro ")
     return helloworld()
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

