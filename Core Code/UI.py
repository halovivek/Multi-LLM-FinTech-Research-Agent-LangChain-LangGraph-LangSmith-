import streamlit as st

st.title("📈 FinTech Multi-LLM Agent")

ticker = st.text_input("Enter Stock Ticker")

if st.button("Analyze"):
    result = run_graph(ticker)
    st.write(result["draft_report"])
