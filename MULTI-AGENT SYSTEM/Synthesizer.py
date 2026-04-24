def synthesizer(state):
    prompt = f"Generate final report: {state}"
    return claude.invoke(prompt).content
