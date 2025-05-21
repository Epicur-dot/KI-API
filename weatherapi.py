import requests
import json

url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 50.9375,
	"longitude": 6.9603,
	"hourly": ["temperature_2m", "uv_index", "rain", "showers"],
	"timezone": "Europe/Berlin",
	"past_days": 2
}

payload ={
    "model":""
}
response = requests.get(url, params=params)
print(response.content)