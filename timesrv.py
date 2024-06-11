from fastapi import FastAPI
from datetime import datetime
app = FastAPI()

@app.get("/time")
def get_time():
    tm = datetime.now().strftime("%H:%M:%S")
    return {'Точное время':tm}

@app.get("/date")
def get_date():
    dt = datetime.now().strftime("%Y:%m:%d")
    return {'Точная дата':dt}