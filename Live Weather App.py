# Import tkinter for creating the graphical user interface (GUI)
import tkinter as tk
# Import messagebox from tkinter to display pop-up messages
from tkinter import messagebox
# Import requests for making HTTP requests to fetch weather data
import requests
# Importing weather_api module (a pyhton file containing the API key) to retrieve the API key. To use this program without any error, please substitute your own API key.
import weather_api as wapi
# Import Image and ImageTk from PIL to handle image processing and displaying in Tkinter
from PIL import Image,ImageTk


# Function to fetch the weather data
def get_weather():
    city = city_entry.get()
    api_key = wapi.openweather_apikey
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Make the API request
        response = requests.get(url)
        data = response.json()

        if data["cod"] == "404":
            # City not found
            messagebox.showerror("Error", "City not found. Please try again.")

        else:
            # Extract data from the API response
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]

            # Extract temperature, pressure, humidity
            temp = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]

            # Extract weather description
            description = weather["description"]

            # Extract wind speed
            wind_speed = wind["speed"]

            # Update the labels with the weather information
            result_label.config(text=f"Temperature: {temp}°C\n"
                                f"Pressure: {pressure} hPa\n"
                                f"Humidity: {humidity}%\n"
                                f"Description: {description.capitalize()}\n"
                                f"Wind Speed: {wind_speed} m/s")
            
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")



# Setting up the GUI
win = tk.Tk()
win.title("Weather App")
win.geometry("550x400")
win.config(bg="#eef3f4")
win.resizable(width="False", height="False")


# Open and resize the image for Live Weather App UI
weatherlogo_img = Image.open('weather_icon.png')
newsize=(60,60)
weatherlogo_img = weatherlogo_img.resize(newsize)
# Convert the image to a format that Tkinter can use (PhotoImage)
weatherlogo_img = ImageTk.PhotoImage(weatherlogo_img,master=win)
# Create a label widget to display the image on the window
weatherlogo_img_lbl = tk.Label(win,image=weatherlogo_img)
weatherlogo_img_lbl.place(relx=.07,rely=0.02)

# Label for the title (or name) of the app
title_label = tk.Label(win, text="Live Weather App", font=("Helvetica", 24, "bold"), bg="#f4f8f9")
title_label.place(relx=0.27, rely=0.024)

# Label for city name
city_label = tk.Label(win, text="Enter City Name: ", font=("Helvetica", 15), bg="#f4f8f9")
city_label.place(relx=0.1, rely=0.24)

# Entry widget for city name
city_entry = tk.Entry(win, font=("Helvetica", 15), width=20, bg="#f4f8f9")
city_entry.place(relx=0.42, rely=0.24)

# Button to fetch weather data
search_button = tk.Button(win,text="Get Weather", font=("Helvetica", 14, "bold"), width=12, border=3, bg="#f4f8f9", command=get_weather)
search_button.place(relx=0.28, rely=0.35)

# Label to display weather results
result_label = tk.Label(win, text="", font=("Helvetica", 15), bg="#f4f8f9")
result_label.place(relx=0.23, rely = 0.52)

# Run the app
win.mainloop()