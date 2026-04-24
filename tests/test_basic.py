from src.main import run


def test_pipeline():
    result = run("AAPL")
    assert "report" in result
