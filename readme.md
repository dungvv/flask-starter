# Flask starter

## Features
- Manage project dependencies with [poetry](https://python-poetry.org)
- Linting and formatting with [mypy](https://mypy.readthedocs.io/en/stable/), [black](https://github.com/psf/black), [autoflake](https://github.com/PyCQA/autoflake), [isort](https://github.com/PyCQA/isort)
- Testing with [pytest](https://pytest.org)

## Managing project dependencies
- (Optional) Create virtual environment: `python3 -m venv venv && source venv/bin/activate`
- Install poetry: `pip install poetry`
- There're 3 groups of dependencies: main, dev, test
- Add to main group: `poetry add <package_name>`
- Add to dev group: `poetry add <package_name> --group dev`
- Add to test group: `poetry add <package_name> --group test`
- Install dependencies for project: `poetry install`

## Linting and formatting
- Format and import: `sh scripts/format-import.sh`
- Lint: `sh scripts/lint.sh`

## Testing
- Pytest auto discover: https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#test-discovery
- File name for testing: `test_*.py` or `*_test.py`
- Write test function with name like: `test*`
- Write test class with name like: `Test*` with test method like `test*`

## Deploying with gunicorn + gevent

## Deploying with bjorne