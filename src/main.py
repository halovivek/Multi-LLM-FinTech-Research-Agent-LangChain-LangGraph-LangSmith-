from src.graph.workflow import build_graph

graph = build_graph()

def run(ticker):
    result = graph.invoke({"ticker": ticker})
    return result


if __name__ == "__main__":
    print(run("AAPL"))
