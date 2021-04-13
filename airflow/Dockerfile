# base image
FROM apache/airflow:2.0.1

ADD requirements.txt /opt/airflow/requirements.txt

RUN pip install -U --upgrade --upgrade-strategy eager -r requirements.txt
