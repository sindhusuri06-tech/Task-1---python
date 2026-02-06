import requests
import matplotlib.pyplot as plt

# Enter your API key here
api_key = "YOUR_API_KEY"

city = "Chennai"

url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

dates = []
temps = []

for i in data["list"][:10]:
    dates.append(i["dt_txt"])
    temps.append(i["main"]["temp"])

plt.figure()
plt.plot(dates, temps)
plt.xticks(rotation=45)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title("Weather Forecast")

plt.tight_layout()
plt.show()
