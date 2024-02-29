USERID=$(shell id -u)
GROUPID=$(shell id -g)

help:
	@echo 'Available commands'
	@echo ''
	@echo 'lock ................................. Generates requirements lock'
	@echo 'migrate .............................. Runs all migrations'
	@echo 'makemigrations ....................... Runs python manage.py makemigrations'
	@echo 'build .................................Build the Docker container'
	@echo 'run .................................. Runs the webserver'

setup: build migrate

build_base_image:
	docker build --tag=school-manager --file=Dockerfile .

build: build_base_image
	docker-compose build

check_rebuild:
	./bin/rebuild.sh

makemigrations: check_rebuild
	./bin/run.sh python manage.py makemigrations

migrate: check_rebuild
	./bin/run.sh python manage.py migrate --no-input

run: check_rebuild
	docker-compose up

collectstatic:
	./bin/run.sh python manage.py collectstatic

# Managing dependencies with pip-tools:
requirements_output = requirements.txt requirements-dev.txt

lock: $(requirements_output)

requirements-dev.txt: requirements.txt

$(requirements_output): %txt: %in
	@docker-compose run app \
		pip-compile -v --generate-hashes --allow-unsafe --no-header --no-emit-index-url --output-file $@ $<