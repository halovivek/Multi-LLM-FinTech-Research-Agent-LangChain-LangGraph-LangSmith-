# Executive Summary

## Project Overview
This project demonstrates an **enterprise-grade financial research system** that orchestrates three frontier Large Language Models (**Gemini, GPT-4, Claude**) through a unified agent architecture built on **LangChain, LangGraph, and LangSmith**. The system performs end-to-end stock analysis — from raw market data ingestion to institutional-grade report generation — with full observability, human oversight, and automated evaluation.

## Key Capabilities

| Capability | Description |
| :--- | :--- |
| **Real-Time Market Data** | Fetches price history, calculates technical indicators (RSI, MACD, Bollinger Bands), and computes risk metrics (VaR, Sharpe Ratio, Max Drawdown). |
| **Parallel Multi-Agent Analysis** | Four specialized agents run simultaneously, each powered by the optimal LLM for its task. |
| **Human-in-the-Loop Approval** | LangGraph interrupts execution for human review before finalizing reports. |
| **Full Observability** | Every LLM call, tool execution, and state transition is traced in LangSmith. |
| **Cost Tracking** | Per-model token usage and cost calculation for optimization. |
| **Interactive UI** | Streamlit web interface for non-technical users. |
