def options_agent(state):
    prompt = f"Analyze OI, PCR, options chain: {state['options']}"
    return gpt.invoke(prompt).content
