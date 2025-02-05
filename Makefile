install:
	@pip install -r requirements.txt

run:
	@python src/main.py

test:
	@pytest tests/

lint:
	@black . && isort . && flake8

clean:
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@rm -rf .pytest_cache
