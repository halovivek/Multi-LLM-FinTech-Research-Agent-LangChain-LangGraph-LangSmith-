import streamlit as st
from src.main import run

st.title("📈 FinGPT Pro")

ticker = st.text_input("Enter NSE Stock (e.g. RELIANCE)")

if st.button("Analyze"):
    result = run(ticker)
    st.write(result["report"])
