from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Sample scooter data
scooters = {"scooter_1": True, "scooter_2": True, "scooter_3": True}  # True means available

class RentRequest(BaseModel):
    scooter_id: str

@app.get("/scooters")
def get_scooters():
    return {"available_scooters": [s for s, available in scooters.items() if available]}

@app.post("/rent")
def rent_scooter(request: RentRequest):
    if request.scooter_id not in scooters:
        raise HTTPException(status_code=404, detail="Scooter not found")
    if not scooters[request.scooter_id]:
        raise HTTPException(status_code=400, detail="Scooter already rented")
    
    scooters[request.scooter_id] = False  # Mark as rented
    return {"message": f"You have rented {request.scooter_id}"}

@app.post("/return")
def return_scooter(request: RentRequest):
    if request.scooter_id not in scooters:
        raise HTTPException(status_code=404, detail="Scooter not found")
    
    scooters[request.scooter_id] = True  # Mark as available
    return {"message": f"You have returned {request.scooter_id}"}
