from __future__ import annotations
import os


def get_timeout() -> int:
try:
return int(os.getenv("HTTP_TIMEOUT", "10"))
except ValueError:
return 10
