from dotenv import load_dotenv
from typing import Tuple, Union

import requests
import os

load_dotenv()

WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")
WEATHER_API_URL_BASE=os.getenv("WEATHER_API_URL_BASE")
USER_ADDRESS = os.getenv("USER_ADDRESS")


def build_display(response: Tuple[bool, Union[dict, str]], user_settings: dict) -> dict:
    try:
        response_dict = {}
        
        response_dict["last_updated"] = response["current"]["last_updated"]
        response_dict["temperature"] = response["current"]["temp_f"] if user_settings["f_c"] == "f" else response["current"]["temp_c"]
        response_dict["feels_like"] = response["current"]["feelslike_f"] if user_settings["f_c"] == "f" else response["current"]["feelslike_c"]
        response_dict["condition"] = response["current"]["condition"]["text"]

        response_dict["wind_speed"] = response["current"]["wind_mph"] if user_settings["mph_kph"] == "mph" else response["current"]["wind_kph"]
        response_dict["wind_degree"] = response["current"]["wind_degree"]
        response_dict["wind_direction"] = response["current"]["wind_dir"]
        response_dict["pressure"] = response["current"]["pressure_mb"] if user_settings["mb_in"] == "mb" else response["current"]["pressure_in"]
        response_dict["humidity"] = response["current"]["humidity"]
        response_dict["cloud"] = response["current"]["cloud"]
        response_dict["wind_chill"] = response["current"]["windchill_f"] if user_settings["f_c"] == "f" else response["current"]["windchill_c"]
        response_dict["heat_index"] = response["current"]["heatindex_f"] if user_settings["f_c"] == "f" else response["current"]["heatindex_c"]
        response_dict["dew_point"] = response["current"]["dewpoint_f"] if user_settings["f_c"] == "f" else response["current"]["dewpoint_c"]
        response_dict["visibility"] = response["current"]["vis_miles"] if user_settings["km_mi"] == "mi" else response["current"]["vis_km"]
        response_dict["uv_index"] = response["current"]["uv"]
        response_dict["gust_spd"] = response["current"]["gust_mph"] if user_settings["mph_kph"] == "mph" else response["current"]["gust_kph"]
        response_dict["air_quality"] = response["current"]["air_quality"]
        
        return response_dict

    except Exception as e:
        print(f"Unknown Exception Building Response: {e}")
        return {"error": str(e)}

def get_current_weather(alerts_on: bool = True) -> Union[dict, str]:
    try:
        url_endpoint = "/current.json"
        url = WEATHER_API_URL_BASE + url_endpoint
        alert = "yes" if alerts_on else "no"

        url = f"{url}?key={WEATHER_API_KEY}&q={USER_ADDRESS}&aqi=yes&lang=en&alerts={alert}"

        response = requests.get(url)
        return response.json()
    
    except Exception as e:
        print(f"Unknown Exception Getting Current Weather: {e}")
        return str(e)
