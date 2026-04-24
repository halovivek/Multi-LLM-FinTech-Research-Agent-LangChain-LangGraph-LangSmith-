from langgraph.graph import StateGraph
from typing import TypedDict

from src.tools.market_data import fetch_stock_data, calculate_rsi, calculate_metrics
from src.agents import data_analyst, risk_analyst, strategist, synthesizer


class State(TypedDict):
    ticker: str
    report: str


def run_pipeline(state):
    data = fetch_stock_data(state["ticker"])
    rsi = calculate_rsi(data)
    metrics = calculate_metrics(data)

    tech = data_analyst.analyze(rsi)
    risk = risk_analyst.analyze(metrics)
    strat = strategist.analyze(tech)

    final = synthesizer.synthesize([tech, risk, strat])

    return {"report": final}


def build_graph():
    builder = StateGraph(State)
    builder.add_node("pipeline", run_pipeline)
    builder.set_entry_point("pipeline")
    return builder.compile()
