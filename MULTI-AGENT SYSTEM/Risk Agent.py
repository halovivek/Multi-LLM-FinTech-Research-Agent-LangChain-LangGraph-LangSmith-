def risk_agent(state):
    prompt = f"Evaluate risk: {state['risk']}"
    return claude.invoke(prompt).content
