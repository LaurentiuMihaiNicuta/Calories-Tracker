import requests
import datetime
from dotenv import load_dotenv
import os

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
NUTRITION_URL = os.getenv("NUTRITION_URL")


today = datetime.datetime.now()

date_str = today.strftime("%d/%m/%Y")
time_str = today.strftime("%H:%M:%S")

user_input = "I swam 2k today!"

data = {
    "query" : user_input
}

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(NUTRI_ENDPOINT,headers=headers,json=data)
workout_data = response.json()["exercises"][0]

sheety_headers = {
    "Authorization": MY_TOKEN,
    "Content-Type": "application/json"
}
data = {
    "workout":{
        "date": date_str,
        "time":  time_str,
        "exercise": workout_data["name"],
        "duration": workout_data["duration_min"],
        "calories": workout_data["nf_calories"]

    }
}


response_sheety = requests.post(SHEETY_ENDPOINT,json=data,headers=sheety_headers)

