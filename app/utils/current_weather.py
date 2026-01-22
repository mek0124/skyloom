from dotenv import load_dotenv
from typing import Tuple, Union
from datetime import datetime

import requests
import json
import sys
import os

load_dotenv()

WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")
WEATHER_API_URL_BASE=os.getenv("WEATHER_API_URL_BASE")
USER_ADDRESS = os.getenv("USER_ADDRESS")


def build_display(response: Tuple[bool, Union[dict, str]], user_settings: dict) -> dict:
    try:
        response_dict = {}
        
        if isinstance(response, tuple):
            if not response[0]:
                return {"error": response[1]}
            data = response[1]
        else:
            data = response
        
        response_dict["last_updated_epoch"] = data["last_updated_epoch"]
        response_dict["last_updated"] = data["last_updated"]
        response_dict["temperature"] = data["temp_f"] if user_settings["f_c"] == "f" else data["temp_c"]
        response_dict["is_day"] = data["is_day"]
        response_dict["condition"] = { "text": data["condition"]["text"], "icon": data["condition"]["icon"] }
        response_dict["wind_speed"] = data["wind_mph"] if user_settings["mph_kph"] == "mph" else data["wind_kph"]
        response_dict["wind_degree"] = data["wind_degree"]
        response_dict["wind_direction"] = data["wind_dir"]
        response_dict["pressure"] = data["pressure_mb"] if user_settings["mb_in"] == "mb" else data["pressure_in"]
        response_dict["humidity"] = data["humidity"]
        response_dict["cloud"] = data["cloud"]
        response_dict["feels_like"] = data["feelslike_f"] if user_settings["f_c"] == "f" else data["feelslike_c"]
        response_dict["wind_chill"] = data["windchill_f"] if user_settings["f_c"] == "f" else data["windchill_c"]
        response_dict["heat_index"] = data["heatindex_f"] if user_settings["f_c"] == "f" else data["heatindex_c"]
        response_dict["dew_point"] = data["dewpoint_f"] if user_settings["f_c"] == "f" else data["dewpoint_c"]
        response_dict["visibility"] = data["vis_miles"] if user_settings["km_mi"] == "mi" else data["vis_km"]
        response_dict["uv_index"] = data["uv"]
        response_dict["gust_spd"] = data["gust_mph"] if user_settings["mph_kph"] == "mph" else data["gust_kph"]
        response_dict["air_quality"] = data["air_quality"]
        response_dict["short_rad"] = data["short_rad"]
        response_dict["diff_rad"] = data["diff_rad"]
        response_dict["dni"] = data["dni"]
        response_dict["gti"] = data["gti"]
        
        return response_dict

    except Exception as e:
        print(f"Unknown Exception Building Response: {e}")
        return {"error": str(e)}

def display_response(response: Tuple[bool, Union[dict, str]], user_settings: dict) -> None:   
    try:
        current_weather = response["current"]
        response_display = build_display(current_weather, user_settings)
        return response_display

    except Exception as e:
        print(f"Unknown Exception Reading Response: {e}")

def store_response(response: Tuple[bool, Union[dict, str]]) -> Tuple[bool, Union[dict, str]]:
    try:
        if not response[0]:
            return response
            
        history_dict = {}
        
        try:
            with open("./output.json", 'r', encoding="utf-8-sig") as history_file:
                history_dict = json.load(history_file)
        
        except FileNotFoundError:
            history_dict = {}
        
        current_date = str(datetime.now().date())
        current_time = str(datetime.now().time())
        
        if current_date not in history_dict:
            history_dict[current_date] = {}
        
        if current_time not in history_dict[current_date]:
            history_dict[current_date][current_time] = []
        
        weather_data = response[1]
        for category in weather_data:
            for key, value in weather_data[category].items():
                history_dict[current_date][current_time].append({
                    "label": key,
                    "value": value
                })
        
        with open("./output.json", 'w', encoding="utf-8-sig") as history_file:
            json.dump(history_dict, history_file, indent=2)

        return True, weather_data

    except Exception as e:
        print(f"Unknown Exception Writing To History File: {e}")
        return False, str(e)

def get_current_weather(alerts: bool) -> Tuple[bool, Union[dict, str]]:
    try:
        url_endpoint = "/current.json"
        url = WEATHER_API_URL_BASE + url_endpoint
        alert = "yes" if alerts else "no"

        url = f"{url}?key={WEATHER_API_KEY}&q={USER_ADDRESS}&aqi=yes&lang=en&alerts={alert}"

        response = requests.get(url)
        return True, response.json()
    
    except Exception as e:
        print(f"Unknown Exception Getting Current Weather: {e}")
        return False, str(e)
