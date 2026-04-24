from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI


def get_gpt():
    return ChatOpenAI(model="gpt-4o", temperature=0.2)


def get_claude():
    return ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.2)


def get_gemini():
    return ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.1)
