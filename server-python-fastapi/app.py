import platform
import mecab
import zlib

from typing import Union
from fastapi import FastAPI

mecab = mecab.MeCab()
app = FastAPI()

@app.get("/")
def read_root():
    return 'Hello World'

@app.get("/health")
def read_health():
    return platform.node()