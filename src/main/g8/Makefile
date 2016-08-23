#
# (c) $year$ $name$
#
# This file is part of $name$,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

.PHONY: help
.DEFAULT_GOAL := help

# ================================================================================
# config
# ================================================================================

DJANGO_SETTINGS_MODULE := $name$.settings_development

DOCKER_IMAGE_NAME := $author$/$name$-server
DOCKER_IMAGE_TAG := latest


# ================================================================================
# setup
# ================================================================================

setup:							## Runs basic setup tasks
	make\
		make-temporary-directory\
		install-python-dependencies\
		install-node-dependencies\
		prepare-database\
		prepare-admin

make-temporary-directory:		## Makes a directory to store temporary files
	mkdir -p temporary

install-python-dependencies:	## Installs Python dependencies
	pip install -r requirements-common.txt
	pip install -r requirements-development.txt

install-node-dependencies:		## Installs Node dependencies
	npm install

prepare-database:				## Makes migrations and applies them to database
	python manage.py makemigrations
	python manage.py migrate

prepare-admin:					## Makes admin user for development use
	PYTHONPATH=\$(shell pwd) DJANGO_SETTINGS_MODULE=\${DJANGO_SETTINGS_MODULE}\
		python ./tools/scripts/create-superuser.py


# ================================================================================
# server
# ================================================================================

run-web-server:					## Runs web server
	DJANGO_SETTINGS_MODULE=\${DJANGO_SETTINGS_MODULE}\
		python manage.py runserver

run-celery-beat:				## Runs Celery Beat
	DJANGO_SETTINGS_MODULE=\${DJANGO_SETTINGS_MODULE}\
		celery -A $name$ beat\
			--no-color\
			--loglevel=DEBUG\
			--schedule=temporary/celerybeat-schedule\
			--pidfile=temporary/celerybeat.pid

run-celery-worker:				## Runs Celery worker
	DJANGO_SETTINGS_MODULE=\${DJANGO_SETTINGS_MODULE}\
		celery -A $name$ worker --concurrency 1 --no-color --loglevel=DEBUG


# ================================================================================
# test
# ================================================================================

run-checks:						## Runs tests and lint
	make run-test run-lint

run-test:						## Runs tests
	py.test

run-lint:						## Runs lint
	flake8


# ================================================================================
# publish
# ================================================================================

embed-git-revision:
	./tools/scripts/render-template.py\
		./$name$/version_template.py\
		git_revision=\$(shell git rev-parse HEAD)\
		> ./$name$/version.py

build-wheel:
	make embed-git-revision
	python setup.py bdist_wheel


build-docker-image:
	make build-wheel
	cp ./dist/*.whl ./docker
	cp ./requirements-production.txt ./docker
	cp ./tools/scripts/create-superuser.py ./docker
	chmod +x ./docker/create-superuser.py
	docker build -t \${DOCKER_IMAGE_NAME}:\${DOCKER_IMAGE_TAG} .


push-docker-image:
	docker push \${DOCKER_IMAGE_NAME}:\${DOCKER_IMAGE_TAG}


# ================================================================================
# help
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
# ================================================================================

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*\$\$' \$(MAKEFILE_LIST)\
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-30s\\033[0m %s\\n", \$\$1, \$\$2}'
