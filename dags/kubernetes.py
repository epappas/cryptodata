
from __future__ import print_function
import os
from pprint import pprint

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

def print_context(ds, **kwargs):
    """Print the Airflow context and ds variable from the context."""
    pprint(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'

with DAG(
    dag_id='kubernetes',
    default_args=args,
    schedule_interval=None,
    start_date=days_ago(2),
    tags=['kubernetes'],
) as dag:

    affinity = {
        'podAntiAffinity': {
            'requiredDuringSchedulingIgnoredDuringExecution': [
                {
                    'topologyKey': 'kubernetes.io/hostname',
                    'labelSelector': {
                        'matchExpressions': [{'key': 'app', 'operator': 'In', 'values': ['airflow']}]
                    },
                }
            ]
        }
    }

    tolerations = [{'key': 'dedicated', 'operator': 'Equal', 'value': 'airflow'}]

    # You don't have to use any special KubernetesExecutor configuration if you don't want to
    start_task = PythonOperator(task_id="start_task", python_callable=print_context, provide_context=True)

    # But you can if you want to
    one_task = PythonOperator(
        task_id="one_task",
        provide_context=True,
        python_callable=print_context,
    )

    # Add arbitrary labels to worker pods
    two_task = PythonOperator(
        task_id="two_task",
        provide_context=True,
        python_callable=print_context,
        executor_config={"KubernetesExecutor": {"labels": {"foo": "bar"}}},
    )

    start_task >> [one_task, two_task]
