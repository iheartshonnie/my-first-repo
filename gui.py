from tkinter import *
from tkinter import ttk  # for dropdown

def launch_form():
    def submit():
        name = name_entry.get()
        age = age_entry.get()
        weather = weather_var.get()
        print(f"Hello {name}, you are {age} years old and you like {weather}.")

    root = tk.Tk()
    root.title("User Form")
    root.geometry("300x250")

    tk.Label(root, text="Enter your name:").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Enter your age:").pack()
    age_entry = tk.Entry(root)
    age_entry.pack()

    tk.Label(root, text="Favorite weather:").pack()
    weather_var = tk.StringVar()
    weather_dropdown = ttk.Combobox(root, textvariable=weather_var)
    weather_dropdown['values'] = ("Sunny", "Rainy", "Snowy")
    weather_dropdown.pack()

    tk.Button(root, text="Submit", command=submit).pack()
    root.mainloop()


def launch_app():
    def fetch_weather():
        city = city_entry.get()
        if not city:
            result_label.config(text="Please enter a city name.")
            return
        try:
            data = get_weather(city)
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            result_label.config(text=f"{city.title()}: {temp}°F, {desc}")
            log_weather(city, temp, desc)
        except Exception as e:
            result_label.config(text=f"Error: {e}")

    root = tk.Tk()
    root.title("Weather App")
    root.geometry("300x200")

    tk.Label(root, text="Enter City:").pack()
    city_entry = tk.Entry(root)
    city_entry.pack()

    tk.Button(root, text="Get Weather", command=fetch_weather).pack()

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()