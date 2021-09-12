# take Airflow base image
FROM apache/airflow:1.10.15-python3.6

# add dags
ADD scripts /opt/airflow/scripts
ADD lib /opt/airflow/lib
ADD dags /opt/airflow/dags
ADD appconfig /opt/airflow/appconfig
ADD tests /opt/airflow/tests
