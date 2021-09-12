# take Airflow base image
FROM apache/airflow:1.10.10-python3.6

# add dags
ADD dags /opt/airflow/dags
ADD appconfig /opt/airflow/appconfig
ADD tests /opt/airflow/tests
