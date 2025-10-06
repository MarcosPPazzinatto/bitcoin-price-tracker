from __future__ import annotations
from math import isfinite


# Simple sparkline using a limited glyph set
_GLYPHS = "▁▂▃▄▅▆▇█"


def sparkline(values: list[float]) -> str:
if not values:
return ""
# Filter out non-finite values
vs = [v for v in values if isfinite(v)]
if not vs:
return ""
lo, hi = min(vs), max(vs)
if hi == lo:
return _GLYPHS[0] * len(vs)
out = []
for v in vs:
idx = int((v - lo) / (hi - lo) * (len(_GLYPHS) - 1))
out.append(_GLYPHS[idx])
return "".join(out)
