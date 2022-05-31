import tkinter as tk
import requests
import time
import config


def get_weather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + \
          "&units=metric&appid=" + config.appid + ""
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = json_data['main']['temp']
    min_temp = json_data['main']['temp_min']
    max_temp = json_data['main']['temp_max']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 3600))
    sunset = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunset'] - 3600))

    final_info = condition + "\n" + str(temp) + " °C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + " °C" + "\n" + "Max Temp: " + str(
        max_temp) + " °C" + "\n" + "Pressure: " + str(pressure) + " hPa" + "\n" + "Humidity: " + str(
        humidity) + "%" + "\n" + "Wind Speed: " + str(wind) +\
                 " m/s" + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("500x600")
canvas.title("Weather App")
canvas.configure(background="light grey")
f = ("Bradley Hand ITC", 20, "bold")
t = ("Baskerville Old Face", 35)

back_color = 'light grey'
textField = tk.Entry(canvas, justify='center', bg=back_color, width=20, font=t, fg="black")
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', get_weather)

label1 = tk.Label(canvas, font=t, fg="black", bg=back_color, pady=10)
label1.pack()
label2 = tk.Label(canvas, bg=back_color, font=f, fg="black")
label2.pack()
canvas.mainloop()
