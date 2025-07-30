import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_news_data():
    url = "https://news.yahoo.co.jp/pickup"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    data = []
    for a in soup.select("li a"):
        title = a.get_text(strip=True)
        link = a.get("href")
        data.append({"タイトル": title, "リンク": link})

    df = pd.DataFrame(data)
    return df

# Streamlit表示部分
st.title("Yahooニュース ピックアップ")
df = get_news_data()
st.dataframe(df)

