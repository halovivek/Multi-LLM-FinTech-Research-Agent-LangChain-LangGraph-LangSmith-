# 🏗 Architecture Document
## Multi-LLM FinTech Research Agent

---

## 1. 📌 Overview

The Multi-LLM FinTech Research Agent is a **production-grade AI system** designed to perform end-to-end financial analysis by combining:

- Real-time market data
- Multi-agent LLM orchestration
- Machine learning models
- Human-in-the-loop validation
- Observability and evaluation

The system transforms raw financial data into **actionable investment insights** through a scalable and modular architecture.

---

## 2. 🎯 Design Goals

---

### 2.1 Scalability
- Modular architecture
- Easy addition of new agents, tools, or models

---

### 2.2 Accuracy
- Multi-LLM specialization
- Data-driven + AI-driven hybrid analysis

---

### 2.3 Observability
- Full tracing via LangSmith
- Monitoring of:
  - LLM calls
  - Tool execution
  - State transitions

---

### 2.4 Cost Efficiency
- Model selection based on task
- Token usage tracking

---

### 2.5 Human Control
- Human-in-the-loop validation before final output

---

## 3. 🧠 High-Level Architecture

┌──────────────────────────────────────────────────────────────┐
│ USER INTERFACE LAYER │
│ Streamlit UI / CLI / API │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ ORCHESTRATION LAYER (LangGraph) │
│ - State Management │
│ - Routing Logic │
│ - Parallel Execution │
└──────────────────────────────────────────────────────────────┘
│
┌───────────────────────┼────────────────────────┐
▼ ▼ ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Data Layer │ │ Agent Layer │ │ ML Layer │
│ (Tools) │ │ (Multi-LLM) │ │ │
│ │ │ │ │ LSTM │
│ NSE APIs │ │ Gemini │ │ Transformer │
│ Indicators │ │ GPT-4 │ │ │
│ Risk Metrics │ │ Claude │ │ │
└──────────────┘ └──────────────┘ └──────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ OBSERVABILITY LAYER (LangSmith) │
│ - Tracing │
│ - Evaluation │
│ - Cost Monitoring │
└──────────────────────────────────────────────────────────────┘


---

## 4. 🧩 System Components

---

### 4.1 User Interface Layer

Provides interaction mechanisms:

- Streamlit dashboard
- CLI interface
- API endpoints (future)

**Responsibilities:**
- Accept user input (ticker, query)
- Display analysis results
- Enable human review

---

### 4.2 Orchestration Layer (LangGraph)

Core execution engine controlling workflow.

**Responsibilities:**
- Maintain system state
- Execute nodes
- Manage routing logic
- Handle parallel execution
- Support interrupts (human-in-loop)

---

### 4.3 Data Layer (Tools)

Handles all data ingestion and preprocessing.

**Components:**
- Market data (NSE APIs / broker APIs)
- Technical indicators (RSI, MACD)
- Risk metrics (Sharpe, VaR)
- News sentiment

---

### 4.4 Agent Layer (Multi-LLM)

Implements specialized AI agents.

| Agent | Model | Responsibility |
|------|------|---------------|
| Technical | Gemini | Indicator analysis |
| Sentiment | Gemini | News analysis |
| Strategy | GPT-4 | Investment reasoning |
| Risk | Claude | Risk evaluation |
| Synthesizer | Claude | Report generation |

---

### 4.5 ML Layer (Optional Enhancement)

Adds predictive capabilities:

- LSTM → Time-series forecasting
- Transformer → Advanced sequence modeling

---

### 4.6 Observability Layer (LangSmith)

Tracks system behavior:

- LLM calls
- Tool usage
- Execution paths
- Token usage and cost

---

## 5. 🔄 Workflow Execution

---

### Step-by-Step Flow

1. User inputs stock ticker  
2. Data collection node fetches:
   - Price data
   - Indicators
   - Risk metrics
   - News  
3. Parallel execution begins:
   - Technical analysis  
   - Risk analysis  
   - Sentiment analysis  
   - Strategy analysis  
4. Outputs are aggregated  
5. Synthesis agent generates draft report  
6. System pauses for human review  
7. Based on feedback:
   - Approve → Final report  
   - Reject → Regenerate  
8. Final output returned  

---

## 6. ⚡ Parallel Execution Model

The system uses **fan-out / fan-in pattern**:

- Fan-out: Multiple agents run simultaneously  
- Fan-in: Results converge for synthesis  

**Benefits:**
- Reduced latency  
- Improved insight quality  
- Efficient resource utilization  

---

## 7. 🔀 LLM Routing Strategy

The system assigns tasks to models based on strengths:

| Task | Model |
|------|------|
| Technical Analysis | Gemini |
| Sentiment | Gemini |
| Strategy | GPT-4 |
| Risk | Claude |
| Synthesis | Claude |

**Key Principle:**
> Use the most suitable model per task instead of a single model.

---

## 8. 👤 Human-in-the-Loop Design

---

### Flow


Draft Report → Human Review → Approve / Reject → Final Output


---

### Features

- Execution pause using LangGraph interrupt
- Feedback-driven iteration
- Maximum retry limit (3)

---

### Benefits

- Increased trust in AI outputs  
- Reduced risk of incorrect insights  
- Human oversight for critical decisions  

---

## 9. 📊 Data Flow

---

### Input

- Stock ticker
- Optional query

---

### Processing

- Data ingestion
- Feature engineering
- Multi-agent analysis
- ML predictions (optional)

---

### Output

- Structured financial report
- Risk insights
- Investment recommendation

---

## 10. ⚙️ Deployment Architecture

---

### Local Deployment

- Python runtime
- Streamlit UI

---

### Containerized Deployment

- Docker
- Docker Compose

---

### Production (Future)

- Cloud deployment (AWS/GCP/Azure)
- Redis / Postgres for state persistence
- Scalable API layer

---

## 11. 📊 Performance Considerations

---

### Latency Optimization

- Parallel execution
- Lightweight models for fast tasks
- Efficient data fetching

---

### Cost Optimization

- Model selection strategy
- Token tracking
- Caching data

---

## 12. 🔒 Security Considerations

---

- API key management via environment variables
- No hardcoded credentials
- Secure data handling

---

## 13. 🏁 Summary

This architecture delivers:

- Multi-LLM intelligence  
- Real-time financial analysis  
- Scalable and modular design  
- Observability-first approach  

It represents a **modern AI system architecture** combining:

- Data engineering  
- Machine learning  
- LLM orchestration  
- Human oversight  

---
