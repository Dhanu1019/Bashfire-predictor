import requests
import matplotlib.pyplot as plt

# Replace with your working API key from WeatherAPI
API_KEY = '3f697cc938f3468a919113938250108'

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "error" in data:
        print("❌ Error fetching weather data:", data.get("error", {}).get("message", "Unknown error"))
        return None

    return {
        'temperature': data['current']['temp_c'],
        'humidity': data['current']['humidity'],
        'wind_speed': data['current']['wind_kph'] / 3.6  # Convert km/h to m/s
    }

def evaluate_risk(temp, humidity, wind):
    if temp > 35 and humidity < 20 and wind > 20:
        return "🔥 CRITICAL"
    elif temp > 30 and humidity < 30:
        return "⚠️ HIGH"
    elif temp > 25:
        return "MEDIUM"
    else:
        return "LOW"

def visualize_data(temp, humidity, wind, risk, city):
    plt.figure(figsize=(7, 4))
    plt.bar(["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"],
            [temp, humidity, wind], color=['red', 'blue', 'orange'])
    plt.title(f"🌡️ Weather in {city} | Bushfire Risk: {risk}")
    plt.ylim(0, max(temp, humidity, wind) + 10)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def main():
    city = input("🌍 Enter city name to check bushfire risk: ")
    print(f"Fetching weather data for {city}...")

    weather = get_weather(city)
    if not weather:
        return

    temp = weather['temperature']
    humidity = weather['humidity']
    wind = weather['wind_speed']

    print(f"\n🌡️ Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🍃 Wind Speed: {wind:.2f} m/s")

    risk = evaluate_risk(temp, humidity, wind)
    print(f"\n🚨 Predicted Bushfire Risk Level in {city}: {risk}")

    visualize_data(temp, humidity, wind, risk, city)

if __name__ == "__main__":
    main()
