import requests

def fetch_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] == "404":
        print("Location not found.")
        return

    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    weather_conditions = weather_data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Conditions: {weather_conditions}")

def main():
    api_key = "abf0391a1e03802d53f476f77d157d3d"  # Replace "YOUR_API_KEY" with your actual API key
    location = input("Enter city name or ZIP code: ")
    weather_data = fetch_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
