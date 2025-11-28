from fastapi import FastAPI
from typing import Union


#"uvicorn fastapi_app:app --reload --port 8000" in cmd, api kann dann unter http://127.0.0.1:8000 erreicht werden

app = FastAPI()

@app.get("/text")
def root():
  return "das ist der text"
