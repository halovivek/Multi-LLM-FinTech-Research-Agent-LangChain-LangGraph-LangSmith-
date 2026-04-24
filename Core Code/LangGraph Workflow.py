builder = StateGraph(FinTechState)

builder.add_node("data_collection", data_collection_node)
builder.add_node("technical", technical_node)
builder.add_node("risk", risk_node)
builder.add_node("strategy", strategy_node)
builder.add_node("sentiment", sentiment_node)
builder.add_node("synthesis", synthesis_node)
builder.add_node("human_review", human_review_node)

builder.set_entry_point("data_collection")

builder.add_edge("data_collection", "technical")
builder.add_edge("data_collection", "risk")
builder.add_edge("data_collection", "strategy")
builder.add_edge("data_collection", "sentiment")

builder.add_edge("technical", "synthesis")
builder.add_edge("risk", "synthesis")
builder.add_edge("strategy", "synthesis")
builder.add_edge("sentiment", "synthesis")

builder.add_edge("synthesis", "human_review")

graph = builder.compile(interrupt_before=["human_review"])
