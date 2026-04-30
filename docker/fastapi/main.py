# app.py

import openai
import time

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "message": "Hello FastAPI"}
