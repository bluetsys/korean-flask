import platform

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World'

@app.route("/health")
def health():
    return platform.node()