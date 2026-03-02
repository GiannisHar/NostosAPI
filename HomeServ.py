from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

BASE_URL = "http://5.172.195.146:5000"
BASE_URL = os.getenv("BASE_URL", "https://server-render-low-ping.onrender.com")

class URLEvent(BaseModel):
    name: str
    userid: str

@app.get("/")
def root():
    return {"message": "Welcome to my api"}

@app.post("/url")
def get_url(event: URLEvent):
    print(event.name)
    print(event.userid)
    return {"URL": BASE_URL}
