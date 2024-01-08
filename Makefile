SHELL=/bin/bash

.DEFAULT_GOAL := help

.PHONY: help
help: ## Shows this help text
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: init
init: clean install test ## Clean environment and reinstall all dependencies

.PHONY: clean
clean: ## Removes project virtual env and untracked files
	rm -rf .venv cdk.out build dist **/*.egg-info .pytest_cache node_modules .coverage
	poetry env remove --all

.PHONY: install
install: ## Install the project dependencies using Poetry.
	poetry install --with test

.PHONY: update
update: ## Update the project dependencies using Poetry.
	poetry update --with test

.PHONY: test
test: ## Run tests
	poetry run python -m pytest

.PHONY: snapshot-update
snapshot-update: ## Run tests and update the snapshots baseline
	poetry run python -m pytest --snapshot-update

.PHONY: synth
synth: ## Synthetize all Cdk stacks
	poetry run cdk synth
