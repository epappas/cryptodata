from datetime import timedelta
import json

from airflow import DAG
from airflow.utils.dates import days_ago

from sample_provider.operators.sample_operator import SampleOperator
from sample_provider.sensors.sample_sensor import SampleSensor

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='sample_worflow',
    default_args=default_args,
    schedule_interval=None,
    start_date=days_ago(2),
    tags=['example'],
) as dag:
    """
    ### Sample DAG

    Showcases the sample provider package's operator and sensor.

    To run this example, create a connector with:
    - id: conn_sample
    - type: http
    - host: www.httpbin.org	
    """

    task_get_op = SampleOperator(
        task_id='get_op',
        sample_conn_id='conn_sample',
        method='get',
    )

    task_sensor = SampleSensor(
        task_id='sensor',
        sample_conn_id='conn_sample',
        endpoint=''
    )

    task_get_op >> task_sensor
