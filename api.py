from __future__ import annotations
import requests
from typing import Any, Dict, List, Tuple
from .utils import get_timeout


COINGECKO = "https://api.coingecko.com/api/v3"


class ApiError(RuntimeError):
pass


def get_price(vs: str = "USD") -> Dict[str, Any]:
vs = vs.lower()
url = f"{COINGECKO}/simple/price"
params = {"ids": "bitcoin", "vs_currencies": vs, "include_last_updated_at": True,
"include_24hr_change": True, "include_24hr_high": True, "include_24hr_low": True}
r = requests.get(url, params=params, timeout=get_timeout())
if not r.ok:
raise ApiError(f"HTTP {r.status_code}: {r.text}")
data = r.json()
if "bitcoin" not in data or vs not in data["bitcoin"]:
raise ApiError("Unexpected API response structure")
return data["bitcoin"]


def get_market_chart(vs: str = "USD", days: int = 1) -> List[Tuple[int, float]]:
vs = vs.lower()
url = f"{COINGECKO}/coins/bitcoin/market_chart"
params = {"vs_currency": vs, "days": days, "precision": 6}
r = requests.get(url, params=params, timeout=get_timeout())
if not r.ok:
raise ApiError(f"HTTP {r.status_code}: {r.text}")
data = r.json()
prices = data.get("prices", [])
# each entry: [timestamp_ms, price]
return [(int(ts), float(price)) for ts, price in prices]
