# Put your app in here.
from flask import Flask, request
from operations import *
app = Flask(__name__)

@app.route('/')
def hey():
    return "hey"
""" 
@app.route('/add')
def add_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{add(a,b)}'

@app.route('/sub')
def sub_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{sub(a,b)}'


@app.route('/mult')
def mult_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{mult(a,b)}'

@app.route('/div')
def div_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{div(a,b)}' """

@app.route('/<ops>')
def ops_rout(ops):
    a = int(request.args['a'])
    b = int(request.args['b'])
    ops_dict = {
        'add': add(a, b),
        'sub': sub(a, b),
        'mult': mult(a, b),
        'div': div(a, b)
    }
    return f'{ops_dict[ops]}'
