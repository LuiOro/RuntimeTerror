import requests
import json
from datetime import datetime
import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.geometry("300x300")
window.title("Weather Station")

# Create labels to display weather data
location_label = tk.Label(window, font=("Calibri", 16))
temperature_label = tk.Label(window, font=("Calibri", 14))
description_label = tk.Label(window, font=("Calibri", 14))
humidity_label = tk.Label(window, font=("Calibri", 14))
wind_speed_label = tk.Label(window, font=("Calibri", 14))
cloud_cover_label = tk.Label(window, font=("Calibri", 14))

# Define a function to get the weather data and update the labels
def get_weather_data():
    # Get the user's input location from the text box
    location = location_entry.get()
    
    # Make an API call to OpenWeatherMap to get the weather data for the given location
    api_key = "YOUR_API_KEY"  # Replace with your own API key from OpenWeatherMap
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(weather_url)
    weather_data = response.json()
    
    # Extract the relevant weather information from the API response
    temperature = round(weather_data['main']['temp'] - 273.15, 2)  # Convert temperature from Kelvin to Celsius
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    cloud_cover = weather_data['clouds']['all']
    
    # Update the labels with the weather information
    location_label.config(text=f"Weather in {location.upper()} as of {datetime.now().strftime('%d %b %Y %I:%M:%S %p')}")
    temperature_label.config(text=f"Temperature: {temperature}°C")
    description_label.config(text=f"Description: {description}")
    humidity_label.config(text=f"Humidity: {humidity}%")
    wind_speed_label.config(text=f"Wind speed: {wind_speed} m/s")
    cloud_cover_label.config(text=f"Cloud cover: {cloud_cover}%")

# Create a label and text box for the location input
location_text = tk.Label(window, text="Enter location:", font=("Calibri", 14))
location_text.pack()
location_entry = tk.Entry(window, font=("Calibri", 14))
location_entry.pack()

# Create a button to get the weather data
get_weather_button = tk.Button(window, text="Get Weather", font=("Calibri", 14), command=get_weather_data)
get_weather_button.pack()

# Pack the weather data labels
location_label.pack()
temperature_label.pack()
description_label.pack()
humidity_label.pack()
wind_speed_label.pack()
cloud_cover_label.pack()

# Start the Tkinter event loop
window.mainloop()
