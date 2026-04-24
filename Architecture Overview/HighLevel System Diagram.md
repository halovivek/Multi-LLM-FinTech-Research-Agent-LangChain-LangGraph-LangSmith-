"""# System Architecture

The system follows a layered architecture with clear separation between the user interface, orchestration engine, data layer, LLM providers, and observability infrastructure.

## Architectural Layers

### 1. User Interface Layer
- **Streamlit App:** The primary web dashboard for end-users.
- **CLI Tool:** For developer interactions and automated scripts.
- **Human Review Console:** A specialized interface for the LangGraph 'interrupt' handler, allowing manual approval of financial reports.

### 2. Orchestration Layer (LangGraph)
- **Router Node:** Directs flow based on user intent.
- **Parallel Analysis Nodes:** Executes multiple specialized agents simultaneously.
- **State Management:** Maintains context and history throughout the analysis lifecycle.

### 3. Data Collection & Processing
- **Financial APIs:** Real-time data ingestion (yfinance, Alpha Vantage).
- **Engineered Metrics:** Automated calculation of RSI, MACD, VaR, and Sharpe Ratios.

### 4. Multi-LLM Provider Layer
- **Google Gemini (Flash/Pro):** Optimized for technical analysis and sentiment scoring.
- **OpenAI GPT-4o:** Utilized for complex strategic reasoning.
- **Anthropic Claude 3.5 Sonnet:** Leveraged for report synthesis and risk assessment.

### 5. Observability & Evaluation (LangSmith)
- **Tracing:** Full lifecycle tracking of every agent action.
- **Cost Tracking:** Per-token and per-model financial monitoring.
- **Evaluation:** Automated testing against golden datasets.
"""
