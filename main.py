from fastapi import FastAPI

app=FastAPI()

@app.get("/all")
def index():
    return "Stocks..!"
