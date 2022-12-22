import platform
import fastapi

from typing import Union
from fastapi import FastAPI, Response, Request

app = FastAPI()

@app.get("/")
def read_root():
    return Response(content='Hello World')
    #return 'Hello World'

@app.get("/health")
def read_health():
    data = {
        "hostname":  platform.node(),
        "language":
        {
            "name": 'python',
            "version": platform.python_version(),
        },
        "web":
        {
            "name": 'flask',
            "version": fastapi.__version__,
        },
    }
    return data