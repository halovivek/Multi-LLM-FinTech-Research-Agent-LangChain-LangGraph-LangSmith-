def get_models():
    return {
        "gemini": ChatGoogleGenerativeAI(model="gemini-2.0-flash"),
        "gpt": ChatOpenAI(model="gpt-4o"),
        "claude": ChatAnthropic(model="claude-3-5-sonnet")
    }
