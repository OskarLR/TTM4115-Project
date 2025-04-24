from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests


app = FastAPI()

API_URL = "http://127.0.0.1:8001"




def get_scooter_status():
    # Send a MQTT request to the scooter to get its status
    # This is a placeholder function. Replace with actual MQTT logic
    #TODO
    pass


# Sample scooter data
scooters = {"scooter_1": {
            "id": "scooter_1",
            "available": True,
            "location": "Downtown",
            "battery": 80,
        },
            "scooter_2": {
            "id": "scooter_2",
            "available": False,
            "location": "Uptown",
            "battery": 50,
        },
            "scooter_3": {
            "id": "scooter_3",
            "available": False,
            "location": "Midtown",
            "battery": 20,
        },
}
class RentRequest(BaseModel):
    scooter_id: str
    

@app.get("/scooters")
def get_scooters():
    # Get all scooters objects if available
    available_scooters = [
        scooter for scooter in scooters.values() if scooter["available"]
    ]
    return {"available_scooters": available_scooters}

@app.post("/rent")
def rent_scooter(request: RentRequest):
    if request.scooter_id not in scooters:
        raise HTTPException(status_code=404, detail="Scooter not found")
    if not scooters[request.scooter_id]:
        raise HTTPException(status_code=400, detail="Scooter already rented")
    
    scooters[request.scooter_id]["available"] = False  # Mark as rented
    response = requests.post(f"{API_URL}/rent")
    return {"message": f"You have rented {request.scooter_id}"}

@app.post("/return")
def return_scooter(request: RentRequest):
    if request.scooter_id not in scooters:
        raise HTTPException(status_code=404, detail="Scooter not found")
    
    scooters[request.scooter_id]["available"] = True  # Mark as available
    response = requests.post(f"{API_URL}/return")
    return {"message": f"You have returned {request.scooter_id}"}
