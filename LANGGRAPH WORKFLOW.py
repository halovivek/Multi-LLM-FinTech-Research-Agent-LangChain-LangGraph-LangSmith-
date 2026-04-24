from langgraph.graph import StateGraph

builder = StateGraph(dict)

builder.add_node("data", data_node)
builder.add_node("technical", technical_agent)
builder.add_node("risk", risk_agent)
builder.add_node("strategy", strategist_agent)
builder.add_node("options", options_agent)
builder.add_node("synthesis", synthesizer)

builder.set_entry_point("data")

builder.add_edge("data", "technical")
builder.add_edge("data", "risk")
builder.add_edge("data", "strategy")
builder.add_edge("data", "options")

builder.add_edge("technical", "synthesis")
builder.add_edge("risk", "synthesis")
builder.add_edge("strategy", "synthesis")
builder.add_edge("options", "synthesis")

graph = builder.compile()
