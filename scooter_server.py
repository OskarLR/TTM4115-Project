from stmpy import Machine, Driver
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()
@app.post("/rent")
def rent_scooter(request):
    # Change STM state to in_use
    escooter.stm.send('unlock')
    # Change light on the scooter
    print("BLINK", flush=True)

@app.post("/return")
def return_scooter(request):
    # Change light on the scooter
    print("BLINK", flush=True)

class Escooter:

    def start_ride(self):
        print('start_ride')



# STMPY
escooter = Escooter()

initial_to_parked = {'source':'initial', 'target':'parked'}
parked_to_in_use = {'trigger':'unlock', 'source':'parked', 'target':'in_use', 'effect':'start_ride'}
parked_to_charging = {'trigger':'connected', 'source':'parked', 'target':'charging', 'effect':'start_charging'}
in_use_to_parked = {'trigger':'parked', 'source':'in_use', 'target':'parked', 'effect':'end_ride'}
parked_to_offline = {'trigger':'turn_off', 'source':'parked', 'target':'offline'}
in_use_to_charging = {'trigger':'connected', 'source':'in_use', 'target':'charging', 'effect':'end_ride;start_charging'}
charging_to_in_use = {'trigger':'unlock', 'source':'charging', 'target':'in_use', 'effect':'stop_charging;start_ride'}

driver = Driver()

stm_escooter = Machine(transitions=[initial_to_parked, 
                                    parked_to_in_use, 
                                    parked_to_charging, 
                                    in_use_to_parked, 
                                    parked_to_offline, 
                                    in_use_to_charging, 
                                    charging_to_in_use], 
                       obj=escooter, name='escooter')

escooter.stm = stm_escooter
driver.add_machine(stm_escooter)
driver.start()

