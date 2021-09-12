.ONESHELL:
SHELL := /bin/bash
.PHONY: all

CWD := $(shell pwd)
PYTHON := $(shell which python3)
PIP := $(PYTHON) -m pip

all: airflow superset

airflow: k8s_config k8s_charts k8s_namespace k8s_airflow

superset: k8s_config k8s_charts k8s_namespace k8s_superset

destroy: k8s_destroy

k8s_config:
	$(CWD)/scripts/0-k8s-config.sh

k8s_charts:
	$(CWD)/scripts/1-k8s-charts.sh

k8s_namespace:
	$(CWD)/scripts/2-k8s-namespace.sh

k8s_airflow:
	$(CWD)/scripts/3-k8s-airflow.sh

k8s_superset:
	$(CWD)/scripts/4-k8s-superset.sh

k8s_pf:
	$(CWD)/scripts/5-k8s-port-forward.sh

k8s_destroy:
	$(CWD)/scripts/6-k8s-destroy.sh

clean:
	$(CWD)/scripts/clean.sh

build:
	$(CWD)/scripts/build.sh

push:
	$(CWD)/scripts/push.sh

scan:
	$(CWD)/scripts/scan.sh

pull:
	$(CWD)/scripts/pull.sh

virtualenv:
	$(PYTHON) -m venv .venv
	@echo Enter the following command to activate your virtualenv:
	@echo source .venv/bin/activate
