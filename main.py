import requests
import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
sheety_Authorization = "Basic c2luYWVzaHJhdGk6c2luYTEzZXNocmF0aTc2"

# --------------------------------------------- Nutritionix API ----------------------------------------
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_params = {
    "query": input("Tell me which exercises you did? ")
}

response = requests.post(nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
data = response.json()
print(data)

# ---------------------------------------- Sheety API ----------------------------------------------------
now = datetime.datetime.now()
now_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%X")

sheety_endpoint = "https://api.sheety.co/42590b54a1ac71c7ac63510780eea096/workoutTracking/workouts"
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": sheety_Authorization
}
for exercise in data["exercises"]:
    sheety_contents = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(sheety_endpoint, json=sheety_contents, headers=sheety_headers)
    print(sheety_response.text)
