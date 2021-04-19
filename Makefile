.ONESHELL:
SHELL := /bin/bash
.PHONY: all

CWD := $(shell pwd)
PYTHON := $(shell which python3)
PIP := $(PYTHON) -m pip

all: build airflow_init

restart: stop run

build:
	$(CWD)/docker/build.sh

push:
	$(CWD)/docker/push.sh postgres
	$(CWD)/docker/push.sh airflow
	$(CWD)/docker/push.sh superset

airflow_init:
	$(CWD)/docker/airflow-init.sh

run:
	$(CWD)/docker/up.sh

run-airflow:
	$(CWD)/docker/airflow-up.sh

run-superset:
	$(CWD)/docker/superset-up.sh

dlogs:
	$(CWD)/docker/logs.sh

stop:
	$(CWD)/docker/stop.sh

clean:
	$(CWD)/docker/clean.sh

virtualenv:
	$(PYTHON) -m venv .venv
	@echo Enter the following command to activate your virtualenv:
	@echo source .venv/bin/activate
