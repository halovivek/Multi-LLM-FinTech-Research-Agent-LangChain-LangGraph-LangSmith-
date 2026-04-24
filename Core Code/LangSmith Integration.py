from langsmith import traceable

@traceable(run_type="llm")
def run_agent(prompt):
    return llm.invoke(prompt)
