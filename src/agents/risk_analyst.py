from src.config.models import get_claude

llm = get_claude()

def analyze(metrics):
    prompt = f"Assess risk: {metrics}"
    return llm.invoke(prompt).content
