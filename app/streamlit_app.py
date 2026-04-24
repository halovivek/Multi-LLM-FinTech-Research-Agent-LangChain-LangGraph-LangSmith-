import streamlit as st
from src.main import run

st.title("📈 Multi-LLM FinTech Agent")

ticker = st.text_input("Enter Stock Ticker")

if st.button("Analyze"):
    result = run(ticker)
    st.write(result["report"])
