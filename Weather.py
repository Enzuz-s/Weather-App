import tkinter as tk
import requests
import time


def get_weather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+\
          "&units=metric&appid=33a0352b584776a021756fadf8895cfe"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = json_data['main']['temp']
    min_temp = json_data['main']['temp_min']
    max_temp = json_data['main']['temp_max']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 7200))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 7200))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("500x600")
canvas.title("Weather App")
canvas.configure(background="light grey")
f = ("Bradley Hand ITC", 20, "bold")
t = ("Baskerville Old Face", 35)


textField = tk.Entry(canvas, justify='center', bg='light grey', width=20, font=t, fg="black")
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', get_weather)

label1 = tk.Label(canvas, font=t, fg="black", bg='light grey', pady=10)
label1.pack()
label2 = tk.Label(canvas, bg='light grey', font=f, fg="black")
label2.pack()
canvas.mainloop()
