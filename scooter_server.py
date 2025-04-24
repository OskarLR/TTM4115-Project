from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.post("/rent")
def rent_scooter(request):
    # Change light on the scooter
    print("BLINK", flush=True)

@app.post("/return")
def return_scooter(request):
    # Change light on the scooter
    print("BLINK", flush=True)