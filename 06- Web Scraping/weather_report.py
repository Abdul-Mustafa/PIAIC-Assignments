import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

# Function to scrape weather data
def scrape_weather_data():
    url = "https://weather.com/en-PK/weather/today/l/PKXX0006:1:PK?Goto=Redirected"  # Replace with the actual weather website URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    cities = soup.select('.city-name')  # Adjust the selector to match the site's structure
    temperatures = soup.select('.temperature')
    conditions = soup.select('.condition')

    for city, temp, condition in zip(cities, temperatures, conditions):
        data.append({
            'City': city.text.strip(),
            'Temperature': float(temp.text.strip().replace('°', '')),
            'Condition': condition.text.strip()
        })

    return pd.DataFrame(data)

# Streamlit application
st.title("Weather Dashboard")

st.write("This dashboard displays weather data for various cities. You can search for a city or sort by temperature.")

# Scrape data
weather_data = scrape_weather_data()

# Add search and sort functionality
search_city = st.text_input("Search for a city:")
sort_option = st.radio("Sort by:", options=["City", "Temperature"])

if search_city:
    filtered_data = weather_data[weather_data['City'].str.contains(search_city, case=False)]
else:
    filtered_data = weather_data

if sort_option:
    filtered_data = filtered_data.sort_values(by=sort_option)

st.table(filtered_data)
