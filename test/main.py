from fastapi import FastAPI
import os
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}