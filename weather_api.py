import requests

geo_coding_url = "https://geocoding-api.open-meteo.com/v1/search"
weather_url = "https://api.open-meteo.com/v1/forecast"
def call_geo_code(name):
    geo_code_dict = {
        "name": name,
        "count": 5,
        "language": "en",
        "format": "json"

    }
    try:
        response = requests.get(
            geo_coding_url,
            params = geo_code_dict,
            timeout = 30
        )
        response.raise_for_status()
        geo_code_data = response.json()
        if "results" not in geo_code_data or not geo_code_data["results"]:
            return None
        else:
            latitude = geo_code_data["results"][0]["latitude"]
            longitude = geo_code_data["results"][0]["longitude"]
            return (latitude, longitude)


    
        
    except requests.RequestException as error:
        print(error)
        return None
def call_weather(latitude, longitude):
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m"
            
    }
    try:
        response = requests.get(
            weather_url,
            params = weather_params
        )
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.RequestException as error:
        print(error)
        return None
    






