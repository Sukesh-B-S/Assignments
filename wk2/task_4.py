import csv
from datetime import datetime
import random

 
# FUNCTION 1: LOG WEATHER DATA (MOCK VERSION)
 
def log_weather(city: str, filename: str):
    """
    Simulates fetching weather data and logs it into a CSV file.
    Returns weather data in dictionary format.
    """

    try:
         
        weather_data = {
            "name": city,
            "main": {
                "temp": round(random.uniform(5, 35), 1),
                "humidity": random.randint(40, 95)
            },
            "wind": {
                "speed": round(random.uniform(1, 15), 1)
            },
            "weather": [
                {"description": "clear sky"}
            ]
        }

        # Current date & time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write data to CSV file
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                city,
                weather_data["main"]["temp"],
                weather_data["main"]["humidity"],
                weather_data["wind"]["speed"],
                weather_data["weather"][0]["description"]
            ])

        return weather_data

    except Exception as e:
        print("Error while logging weather:", e)

  
  #ANALYZE WEATHER DATA
 
def analyze_weather(weather_data: dict) -> str:
    """
    Analyzes weather data and returns a readable summary.
    """

    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind = weather_data["wind"]["speed"]

    summary = ""

    # Temperature analysis
    if temp <= 10:
        summary = "Cold (≤10°C)"
    elif 11 <= temp <= 24:
        summary = "Mild (11–24°C)"
    else:
        summary = "Hot (≥25°C)"

    # Weather warnings
    if wind > 10:
        summary += " | High wind alert!"
    if humidity > 80:
        summary += " | Humid conditions!"

    return summary


 
# MAIN PROGRAM
 
if __name__ == "__main__":

    file_name = "weather_log.csv"
    city = input("Enter city name: ")

    weather = log_weather(city, file_name)

    if weather:
        analysis = analyze_weather(weather)
        print("\nWeather Analysis Result:")
        print(analysis)
