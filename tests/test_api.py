from src.btc_tracker.api import get_price


def test_price_basic():
data = get_price("usd")
assert "usd" in data
assert isinstance(data["usd"], (int, float))
