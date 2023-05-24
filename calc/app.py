# Put your app in here.
from flask import Flask
from operations import *
app = Flask(__name__)

@app.route(f'/add?a=<a>&b=<b>')
def add_route(a,b):
    return add(a,b)