from src.config.models import get_gpt

llm = get_gpt()

def analyze(context):
    prompt = f"Provide investment strategy: {context}"
    return llm.invoke(prompt).content
