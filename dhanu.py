import requests
import streamlit as st

# Your WeatherAPI key here
API_KEY = "3f697cc938f3468a919113938250108"  # Replace with your actual API key

# Function to get weather data from API
def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "error" in data:
        return None, data.get("error", {}).get("message", "Unknown error")

    return {
        'temperature': data['current']['temp_c'],
        'humidity': data['current']['humidity'],
        'wind_speed': data['current']['wind_kph'] / 3.6  # converting kph to m/s
    }, None

# Function to evaluate bushfire risk level
def evaluate_risk(temp, humidity, wind):
    if temp > 35 and humidity < 20 and wind > 20:
        return "CRITICAL"
    elif temp > 30 and humidity < 30:
        return "HIGH"
    elif temp > 25:
        return "MEDIUM"
    else:
        return "LOW"

# Streamlit app layout
st.set_page_config(page_title="Bushfire Risk Predictor", layout="centered")
st.title("Bushfire Risk Predictor")
st.write("This app predicts bushfire risk level using real-time weather data like temperature, humidity, and wind speed.")

# User input
city = st.text_input("Enter City Name")

# Button to trigger prediction
if st.button("Check Risk"):
    weather, error = get_weather(city)

    if error:
        st.error(f"API Error: {error}")
    else:
        temp = weather['temperature']
        humidity = weather['humidity']
        wind = weather['wind_speed']
        risk = evaluate_risk(temp, humidity, wind)

        st.subheader("Weather Conditions")
        st.markdown(f"City: **{city}**")
        st.markdown(f"Temperature: **{temp} °C**")
        st.markdown(f"Humidity: **{humidity} %**")
        st.markdown(f"Wind Speed: **{wind:.2f} m/s**")

        st.subheader("Bushfire Risk Assessment")
        st.markdown(f"Risk Level: **{risk}**")

        st.subheader("Weather Data Chart")
        st.bar_chart({
            "Metrics": {
                "Temperature (°C)": temp,
                "Humidity (%)": humidity,
                "Wind Speed (m/s)": wind
            }
        })
