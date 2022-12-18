# save this as app.py
from flask import Flask, request
import mecab
import platform

mecab = mecab.MeCab()

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return platform.node()

@app.route('/user/<user_name>/<int:user_id>')
def user1(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'

@app.route('/', methods=['POST'])
def mainpost():
    a = request.data

    return mecab.nouns(a)