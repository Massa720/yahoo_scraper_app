import streamlit as st
from scraper import get_news_data  # scraper.pyにこの関数がある前提

st.title("Yahooニュース ピックアップ")

df = get_news_data()
st.dataframe(df)
