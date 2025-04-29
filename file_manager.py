import datetime

def log_weather(city, temp, desc):
    now = datetime.datetime.now()
    with open("weather_log.txt", "a") as file:
        file.write(f"{now} - {city.title()}: {temp}°F, {desc}\n")