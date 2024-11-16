import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

# Function to scrape news articles
def scrape_news_data():
    url = "https://www.nbcnews.com/"  # Replace with the actual news website URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    articles = soup.select('.article')  # Adjust the selector to match the site's structure
    for article in articles:
        title = article.select_one('.title').text.strip()  # Adjust selector
        date = article.select_one('.date').text.strip()    # Adjust selector
        summary = article.select_one('.summary').text.strip()  # Adjust selector
        data.append({
            'Title': title,
            'Date': date,
            'Summary': summary
        })

    return pd.DataFrame(data)

# Streamlit application
st.title("News Dashboard")

st.write("Explore the latest news articles. Filter by date or search for specific categories.")

# Scrape data
news_data = scrape_news_data()

# Add date and category filters
date_filter = st.date_input("Filter by date:")
if date_filter:
    news_data['Date'] = pd.to_datetime(news_data['Date'])
    filtered_data = news_data[news_data['Date'] == pd.to_datetime(date_filter)]
else:
    filtered_data = news_data

st.table(filtered_data)
