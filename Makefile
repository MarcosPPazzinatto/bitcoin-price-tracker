.PHONY: fmt lint test run


fmt:
python -m pip install black
black src tests


lint:
python -m pip install flake8
flake8 src tests


test:
python -m pip install -r requirements.txt pytest
pytest


run:
python -m src.btc_tracker.cli price --vs USD
