from src.config.models import get_claude

llm = get_claude()

def synthesize(inputs):
    prompt = f"Combine into final report: {inputs}"
    return llm.invoke(prompt).content
