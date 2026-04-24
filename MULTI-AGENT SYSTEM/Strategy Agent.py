def strategist_agent(state):
    prompt = f"Give investment thesis: {state}"
    return gpt.invoke(prompt).content
