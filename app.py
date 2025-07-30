import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(__file__))
from scraper import get_news_data  # ←ここでエラー解決！

st.title("Yahooニュース ピックアップ")

df = get_news_data()
st.dataframe(df)
