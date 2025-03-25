import os
import sys
import pytest

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from helpers.api_utils import get_weather_by_city, get_weather_by_coordinates, get_forecast_by_city

@pytest.fixture(autouse=True)
def check_api_key():
    """Ensure API key is set before running tests"""
    from config import config
    if not config.API_KEY or config.API_KEY == "your-api-key-here":
        pytest.skip("API key not configured")

from config.config import API_KEY

class TestWeatherAPI:
    def test_get_weather_by_city_valid(self):
        city_name = "London"
        response = get_weather_by_city(city_name)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == city_name
        assert "main" in data
        assert "weather" in data

    def test_get_weather_by_city_invalid_city(self):
        city_name = "InvalidCityName123"
        response = get_weather_by_city(city_name)
        assert response.status_code == 404
        data = response.json()
        assert data["cod"] == "404"

    def test_get_weather_by_coordinates_valid(self):
        lat = 51.5074
        lon = 0.1278
        response = get_weather_by_coordinates(lat, lon)
        assert response.status_code == 200
        data = response.json()
        assert abs(data["coord"]["lat"] - lat) < 0.1  # Allow for slight variations
        assert abs(data["coord"]["lon"] - lon) < 0.1

    def test_get_weather_by_city_fahrenheit(self):
        city_name = "New York"
        response = get_weather_by_city(city_name, units="imperial")
        assert response.status_code == 200
        data = response.json()
        assert "main" in data
        assert "temp" in data["main"]
        assert data["main"]["temp"] > 200  # Expecting temperature in Fahrenheit

    def test_get_forecast_by_city_valid(self):
        city_name = "Paris"
        response = get_forecast_by_city(city_name)
        assert response.status_code == 200
        data = response.json()
        assert data["city"]["name"] == city_name
        assert len(data["list"]) > 0

    def test_get_weather_by_city_invalid_api_key(self):
        # Temporarily modify API_KEY for this test
        from config import config
        original_api_key = config.API_KEY
        config.API_KEY = "INVALID_KEY"
        try:
            city_name = "London"
            response = get_weather_by_city(city_name)
            assert response.status_code == 401
            data = response.json()
            assert data["cod"] == 401
        finally:
            config.API_KEY = original_api_key # Restore the original API key