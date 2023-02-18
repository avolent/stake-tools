.PHONY: local requirements

local: requirements
	pipenv shell

requirements:
	pipenv install