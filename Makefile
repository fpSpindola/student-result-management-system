USERID=$(shell id -u)
GROUPID=$(shell id -g)

help:
    @echo 'Available commands:'
	@echo ''
	@echo 'lock ................................. Generates requirements lock'
	@echo 'migrate .............................. Runs all migrations'
	@echo 'makemigrations ....................... Runs python manage.py makemigrations'
	@echo 'build .................................Build the Docker container'
	@echo 'run .................................. Runs the webserver'

setup: build migrate collectstatic

build_base_image:
	docker build --tag=school-manager --file=Dockerfile .

build: build_base_image
	docker-compose build

collectstatic:
    ./bin/run.sh python manage.py collectstatic

lock: $(requirements_output)

requirements-dev.txt: requirements.txt

$(requirements_output): %txt: %in
	@docker-compose run -e PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} web \
		pip-compile -v --generate-hashes --allow-unsafe --no-header --no-emit-index-url --output-file $@ $<