# 🔧 Low-Level Design (LLD)
## Multi-LLM FinTech Research Agent

---

## 1. 📌 Overview

This document describes the **internal implementation details** of the system, including:

- State schema (single source of truth)
- Node-level execution logic
- Edge routing and control flow
- Prompt design for each LLM agent

The system is implemented using **LangGraph** for orchestration and **LangChain** for model interaction.

---

## 2. 🧠 State Schema (FinTechState)

The system uses a centralized state object passed between nodes.

### 📄 Definition

```python
from typing import TypedDict, Optional, List, Dict, Any

class FinTechState(TypedDict):
    # Input
    ticker: str
    query: str
    analysis_type: str

    # Data Layer
    price_data: Optional[Dict[str, Any]]
    technical_indicators: Optional[Dict[str, Any]]
    risk_metrics: Optional[Dict[str, float]]
    news_data: Optional[List[Dict]]

    # Agent Outputs
    technical_analysis: Optional[str]
    risk_assessment: Optional[str]
    sentiment_analysis: Optional[str]
    strategic_analysis: Optional[str]

    # Final Output
    draft_report: Optional[str]
    final_report: Optional[str]

    # Control
    human_feedback: Optional[str]
    status: str
    iteration: int

    # Observability
    model_usage: Dict[str, Any]
    error_message: Optional[str]

    🧩 Design Notes
Acts as single source of truth
Enables stateful execution across nodes
Supports:
Parallel execution
Iterative loops (human-in-loop)
Observability
3. ⚙️ Node-Level Logic

Each node represents a functional unit in the workflow.

def data_collection_node(state: FinTechState):
    data = fetch_stock_data(state["ticker"])
    indicators = calculate_indicators(data)
    risk = calculate_risk(data)
    news = fetch_news(state["ticker"])

    return {
        "price_data": data,
        "technical_indicators": indicators,
        "risk_metrics": risk,
        "news_data": news,
        "status": "analyzing"
    }

🧩 Design Notes
Acts as single source of truth
Enables stateful execution across nodes
Supports:
Parallel execution
Iterative loops (human-in-loop)
Observability
3. ⚙️ Node-Level Logic

Each node represents a functional unit in the workflow.
def data_collection_node(state: FinTechState):
    data = fetch_stock_data(state["ticker"])
    indicators = calculate_indicators(data)
    risk = calculate_risk(data)
    news = fetch_news(state["ticker"])

    return {
        "price_data": data,
        "technical_indicators": indicators,
        "risk_metrics": risk,
        "news_data": news,
        "status": "analyzing"
    }

def technical_node(state: FinTechState):
    result = gemini.invoke(build_technical_prompt(state))
    return {"technical_analysis": result.content}

def risk_node(state: FinTechState):
    result = claude.invoke(build_risk_prompt(state))
    return {"risk_assessment": result.content}

def sentiment_node(state: FinTechState):
    result = gemini.invoke(build_sentiment_prompt(state))
    return {"sentiment_analysis": result.content}

def strategy_node(state: FinTechState):
    result = gpt.invoke(build_strategy_prompt(state))
    return {"strategic_analysis": result.content}

def synthesis_node(state: FinTechState):
    result = claude.invoke(build_synthesis_prompt(state))
    return {"draft_report": result.content}

def human_review_node(state: FinTechState):
    return {"status": "review"}

def finalize_node(state: FinTechState):
    return {
        "final_report": state["draft_report"],
        "status": "completed"
    }
Edge Routing Logic

Routing is implemented using LangGraph conditional edges.
def route_from_start(state: FinTechState):
    return "data_collection"

Parallel Execution
After data collection:
builder.add_edge("data_collection", "technical")
builder.add_edge("data_collection", "risk")
builder.add_edge("data_collection", "sentiment")
builder.add_edge("data_collection", "strategy")

Synchronization

All analysis nodes converge into synthesis:
builder.add_edge("technical", "synthesis")
builder.add_edge("risk", "synthesis")
builder.add_edge("sentiment", "synthesis")
builder.add_edge("strategy", "synthesis")

Human-in-the-Loop Routing
def route_after_review(state: FinTechState):
    feedback = (state.get("human_feedback") or "").lower()
    iteration = state.get("iteration", 0)

    if feedback in ["reject", "revise"] and iteration < 3:
        return "synthesis"
    return "finalize"

Interrupt Configuration
graph = builder.compile(
    interrupt_before=["human_review"]
)

Prompt Design per Agent

Each agent follows a structured prompt pattern:
Technical Analysis Prompt (Gemini)
def build_technical_prompt(state):
    return f"""
You are a quantitative analyst.

Ticker: {state['ticker']}
RSI: {state['technical_indicators']['rsi']}
MACD: {state['technical_indicators']['macd']}

Analyze:
- Trend direction
- Overbought/oversold signals
- Key patterns
"""
5.2 Risk Analysis Prompt (Claude)
def build_risk_prompt(state):
    return f"""
You are a risk analyst.

Volatility: {state['risk_metrics']['volatility']}
Sharpe Ratio: {state['risk_metrics']['sharpe']}

Evaluate:
- Downside risk
- Risk category
- Tail risk scenarios
"""

Sentiment Prompt (Gemini)
def build_sentiment_prompt(state):
    return f"""
Analyze sentiment from news:

Articles: {state['news_data']}

Return:
- Sentiment score
- Key themes
"""

Strategy Prompt (GPT-4)
def build_strategy_prompt(state):
    return f"""
You are an investment strategist.

Inputs:
- Technical: {state['technical_analysis']}
- Risk: {state['risk_assessment']}
- Sentiment: {state['sentiment_analysis']}

Provide:
- Investment thesis
- Short-term vs long-term view
"""

Synthesis Prompt (Claude)
def build_synthesis_prompt(state):
    return f"""
Generate a structured financial report:

Technical: {state['technical_analysis']}
Risk: {state['risk_assessment']}
Strategy: {state['strategic_analysis']}
Sentiment: {state['sentiment_analysis']}

Output:
- Executive summary
- Key insights
- Final recommendation
"""
Observability Hooks
Each node logs:
Input state
Output state
Model usage
Integrated with LangSmith via:
@traceable(run_type="chain")

Summary

This LLD defines:

A state-driven execution model
Modular node-based processing
Flexible routing and control flow
Structured prompt engineering

The design ensures:

Scalability
Observability
Maintainability

# ✅ Why This Works

This LLD shows:

- Real system internals (not generic fluff)
- Clear data flow (state-driven)
- Strong engineering thinking
- Direct mapping to LangGraph implementation
