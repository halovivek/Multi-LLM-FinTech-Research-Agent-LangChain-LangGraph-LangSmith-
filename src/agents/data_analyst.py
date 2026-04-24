from src.config.models import get_gemini

llm = get_gemini()

def analyze(data):
    prompt = f"Analyze stock technicals: {data}"
    return llm.invoke(prompt).content
