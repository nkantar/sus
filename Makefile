.DEFAULT_GOAL := help
.PHONY: help formatcheck docstylecheck typecheck lint test


help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


formatcheck: ## run format check via black
	poetry run black src/ tests/ --check


docstylecheck: ## run docstyle check via pydocstyle
	poetry run docstylecheck


typecheck: ## run type check via mypy
	poetry run mypy src/ --strict


lint: ## run linter (flake8)
	poetry run flake8


test: ## run tests
	poetry run pytest
