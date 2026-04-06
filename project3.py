import requests

api_key = "f51945a205faa858ec37b43cc1827af4"
base_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(base_url, params=params)
data = response.json()

if response.status_code == 200:
    print(f"\nWeather in {city}:")
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Condition:", data["weather"][0]["description"])
else:
    print("\nError:", data.get("message", "Something went wrong."))