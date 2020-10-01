.DEFAULT_GOAL := help
.PHONY: help formatcheck docstylecheck typecheck lint test all install publish publish-test


help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


formatcheck: ## run format check via black
	poetry run black src/ tests/ --check


docstylecheck: ## run docstyle check via pydocstyle
	poetry run pydocstyle src/


typecheck: ## run type check via mypy
	poetry run mypy src/ --strict


lint: ## run linter (flake8)
	poetry run flake8 src/


test: ## run tests
	poetry run pytest tests/


all: ## run all validation
	make formatcheck
	make docstylecheck
	make typecheck
	make lint
	make test

install: ## install all dependencies (including dev)
	poetry install

package: ## create wheel and tarball for PyPI
	poetry build

publish: ## publish on PyPI
	poetry publish

publish-test: ## publish on TestPyPI
	poetry publish -r testpypi
