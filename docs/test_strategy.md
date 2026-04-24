# 🧪 Test Strategy
## Multi-LLM FinTech Research Agent

---

## 1. 📌 Overview

This document defines the testing approach for the Multi-LLM FinTech Research Agent system.

The testing strategy ensures:
- Functional correctness
- System reliability
- AI output quality
- Performance and cost control

The system is tested across three layers:
1. Unit Testing (Tools)
2. Integration Testing (Graph Workflow)
3. LLM Evaluation (LangSmith)

---

## 2. 🧩 Test Types

---

## 2.1 🔬 Unit Testing (Tools Layer)

### 📌 Objective
Validate correctness of individual data processing and computation functions.

---

### 🧪 Scope

- Market data fetching
- Technical indicators
- Risk calculations
- Options / financial utilities

---

### 📂 Test Files

---

### ✅ Key Test Cases

#### 1. RSI Calculation

```python
def test_rsi():
    data = mock_price_data()
    rsi = calculate_rsi(data)
    assert 0 <= rsi <= 100

def test_sharpe_ratio():
    returns = [0.01, -0.02, 0.015]
    sharpe = calculate_sharpe(returns)
    assert isinstance(sharpe, float)

def test_fetch_data():
    data = fetch_stock_data("AAPL")
    assert not data.empty

Validation Criteria
Output correctness
Data type validation
Edge case handling (empty data, NaN)
2.2 🔗 Integration Testing (Graph Workflow)
📌 Objective

Ensure the end-to-end workflow execution behaves correctly across nodes and edges.

🧪 Scope
Graph compilation
Node execution flow
State transitions
Routing logic
📂 Test Files
tests/test_graph.py
✅ Key Test Cases
1. Graph Compilation
def test_graph_build():
    graph = build_graph()
    assert graph is not None
2. End-to-End Execution
def test_full_pipeline():
    result = graph.invoke({"ticker": "AAPL"})
    assert "final_report" in result
3. Routing Logic
def test_routing():
    state = {"analysis_type": "stock"}
    next_node = route_from_start(state)
    assert next_node == "data_collection"
4. Parallel Execution Validation
Ensure all agent outputs exist:
technical_analysis
risk_assessment
sentiment_analysis
strategic_analysis
🎯 Validation Criteria
Correct node transitions
No deadlocks in workflow
All required outputs generated
Proper error handling
2.3 🤖 LLM Evaluation (LangSmith)
📌 Objective

Evaluate quality, consistency, and relevance of AI-generated outputs.

🧪 Scope
Report completeness
Insight quality
Consistency across runs
Prompt effectiveness
⚙️ Tools Used
LangSmith datasets
Custom evaluators
📂 Files
src/evaluation/eval_dataset.py
src/evaluation/evaluators.py
📊 Evaluation Metrics
1. Content Coverage

Checks if report includes:

Technical analysis
Risk assessment
Strategy
Sentiment
def contains_expected_content(output):
    return all(section in output for section in ["Technical", "Risk", "Strategy"])
2. Report Depth

Measures richness of output:

Minimum word count
Structured explanation
def report_depth(output):
    return len(output.split()) > 300
3. Relevance Score
Alignment with input ticker
Logical consistency
🎯 Validation Criteria
≥ 85% relevance score
Structured and complete output
No hallucinated financial facts
3. ⚡ Performance Testing
📌 Metrics
Latency per run
Token usage
Cost per execution
🧪 Example
def test_latency():
    start = time.time()
    run("AAPL")
    end = time.time()

    assert (end - start) < 8
4. 💰 Cost Testing
📌 Objective

Ensure system remains cost-efficient.

Validation
Track tokens per model
Ensure total cost < target threshold
5. 🧱 CI/CD Integration
GitHub Actions Pipeline

Runs automatically on:

Push
Pull Request
Steps
Install dependencies
Run unit tests
Run integration tests
Lint code
Example
- run: pytest
6. 🚨 Error Handling Tests
Scenarios
Missing data
API failures
Invalid ticker
LLM failure
Expected Behavior
Graceful fallback
Error logged in state
No system crash
7. 🏁 Summary

This test strategy ensures:

Reliable data processing (Unit Tests)
Correct system behavior (Integration Tests)
High-quality AI outputs (LLM Evaluation)

The combination of:

Deterministic testing
AI evaluation
Observability

ensures the system is production-ready and scalable.


---

# ✅ Why This Works

This document shows:

- You understand **testing beyond code (AI evaluation)**
- You know **LangSmith usage (rare skill)**
- You think in **systems, not scripts**
