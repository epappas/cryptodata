.ONESHELL:
SHELL := /bin/bash
.PHONY: all

CWD := $(shell pwd)
PYTHON := $(shell which python3)
PIP := $(PYTHON) -m pip

all: build airflow_init

restart: stop run

build:
	@docker-compose build

push:
	$(CWD)/docker/push.sh postgres
	$(CWD)/docker/push.sh airflow
	$(CWD)/docker/push.sh superset

airflow_init:
	$(CWD)/docker/airflow-init.sh

run:
	@docker-compose up -d

dlogs:
	@docker-compose logs -f -t

stop:
	@docker-compose down --remove-orphans

clean:
	@docker-compose down --volumes --rmi all --remove-orphans

virtualenv:
	$(PYTHON) -m venv .venv
	@echo Enter the following command to activate your virtualenv:
	@echo source .venv/bin/activate
