def technical_agent(state):
    prompt = f"Analyze RSI, MACD: {state['technical']}"
    return gemini.invoke(prompt).content
