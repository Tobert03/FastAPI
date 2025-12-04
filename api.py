from fastapi import FastAPI
from typing import Union
import sqlite3


#"uvicorn fastapi_app:app --reload --port 8000" in cmd, api kann dann unter http://127.0.0.1:8000 erreicht werden

app = FastAPI()

@app.get("/text")
def root():
  return "das ist der text"



@app.put("/new_item/{product_name}")
def new_item(product_name: str):
  conn = sqlite3.connect("database.db")
  cursor = conn.cursor()
  try:
    cursor.execute( "INSERT INTO inventory (product_name) VALUES (?)", (product_name,) )

    conn.commit()

    return {"message": f"Neues item '{product_name}' wurde hinzugefügt"}
  except Exception as e:
    return {"message": f"Neues item '{product_name}' konnte nicht hinzugefügt werden"}