
from fastapi import FastAPI
from app.addition import add_numbers

app = FastAPI(title="Python Addition API")


@app.get("/")
def home():
    return {"message": "Welcome to Python Addition API"}


@app.get("/add")
def addition(a: float, b: float):
    result = add_numbers(a, b)

    return {
        "number1": a,
        "number2": b,
        "addition": result
    }
