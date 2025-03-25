import requests
from config.config import BASE_URL, API_KEY

def get_weather_by_city(city_name, units="metric"):
    """Get current weather for a city"""
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": units
    }
    response = requests.get(f"{BASE_URL}/weather", params=params)
    return response

def get_weather_by_coordinates(lat, lon, units="metric"):
    """Get current weather for coordinates"""
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": units
    }
    response = requests.get(f"{BASE_URL}/weather", params=params)
    return response

def get_forecast_by_city(city_name, units="metric"):
    """Get 5-day forecast for a city"""
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": units
    }
    response = requests.get(f"{BASE_URL}/forecast", params=params)
    return response
