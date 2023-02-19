.PHONY: local requirements run

local: requirements
	pipenv shell

requirements:
	pipenv install

run:
	python app/app.py