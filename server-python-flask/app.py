import platform
import mecab
import zlib

from flask import Flask, request

mecab = mecab.MeCab()
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return platform.node()

@app.route("/health")
def health():
    return platform.node()

# @app.route('/', methods=['POST'])
# def mainpost():
#     a = request.data

#     return mecab.nouns(a)