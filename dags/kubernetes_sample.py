from airflow import DAG
from datetime import datetime
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime.utcnow(),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}

dag = DAG("kubernetes_sample", default_args=default_args, schedule_interval="@once",)


start = DummyOperator(task_id="run_this_first", dag=dag)

# intentionally pointing to "airflow" kubernetes namespace to illustrate that pods can run in different environments
# "airflow" should work for cloud composer as well
passing_python = KubernetesPodOperator(
    namespace="airflow",
    image="python:3.7-slim",
    cmds=["python", "-c"],
    arguments=["print('hello world')"],
    labels={"foo": "bar"},
    name="passing-python",
    task_id="passing-python-task",
    get_logs=True,
    dag=dag,
)

passing_bash = KubernetesPodOperator(
    namespace="airflow",
    image="ubuntu:16.04",
    cmds=["/bin/bash", "-cx"],
    arguments=["echo hello world"],
    labels={"foo": "bar"},
    name="fail",
    task_id="passing-bash-task",
    get_logs=True,
    dag=dag,
)

start >> [passing_python, passing_bash]
