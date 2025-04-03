import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # Adjust if hosted elsewhere

st.title("E-Scooter Rental Service")

if st.button("Check Available Scooters"):
    response = requests.get(f"{API_URL}/scooters")
    available = response.json().get("available_scooters", [])
    st.write("Available Scooters:", available)

scooter_id = st.text_input("Enter Scooter ID to Rent/Return")

if st.button("Rent Scooter"):
    response = requests.post(f"{API_URL}/rent", json={"scooter_id": scooter_id})
    st.write(response.json().get("message", "Error"))

if st.button("Return Scooter"):
    response = requests.post(f"{API_URL}/return", json={"scooter_id": scooter_id})
    st.write(response.json().get("message", "Error"))
