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

install:
	$(CWD)/docker/meltano.sh install

airflow_init:
	$(CWD)/docker/airflow_init.sh

run:
	@docker-compose up -d

logs:
	@docker-compose logs -f -t

stop:
	@docker-compose down --remove-orphans

clean:
	@docker-compose down --volumes --rmi all --remove-orphans

virtualenv:
	$(PYTHON) -m venv .venv
	@echo Enter the following command to activate your virtualenv:
	@echo source .venv/bin/activate

dev_env:
	$(PIP) install -r requirements.txt

