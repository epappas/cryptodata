"""An example DAG demonstrating Kubernetes Pod Operator."""

import datetime

from airflow import models
from kubernetes.client import models as k8s
from airflow.kubernetes.secret import Secret
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

secret_env = Secret(
    # Expose the secret as environment variable.
    deploy_type='env',
    # The name of the environment variable, since deploy_type is `env` rather
    # than `volume`.
    deploy_target='SQL_CONN',
    # Name of the Kubernetes Secret
    secret='airflow-secrets',
    # Key of a secret stored in this Secret object
    key='sql_alchemy_conn')
secret_volume = Secret(
    deploy_type='volume',
    # Path where we mount the secret as volume
    deploy_target='/var/secrets/google',
    # Name of Kubernetes Secret
    secret='service-account',
    # Key in the form of service account file name
    key='service-account.json')

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

# If a Pod fails to launch, or has an error occur in the container, Airflow
# will show the task as failed, as well as contain all of the task logs
# required to debug.
with models.DAG(
        dag_id='tap_cryptodata',
        schedule_interval=datetime.timedelta(days=1),
        start_date=YESTERDAY) as dag:


    start = DummyOperator(task_id="tap_cryptodata_start", dag=dag)

    tap_cryptodata = KubernetesPodOperator(
        task_id="tap-cryptodata-task",
        name="tap-cryptodata",
        namespace="airflow",
        image="epappas/tap-cryptodata:latest",
        cmds=["tap-cryptodata"],
        arguments=["-c", "./sample_config.json"],
        labels={"foo": "bar"},
        get_logs=True,
        affinity={},
        dag=dag)
        # arguments=['{{ ds }}'],
        # env_vars={'MY_VALUE': '{{ var.value.my_value }}'},
        # config_file="{{ conf.get('core', 'kube_config') }}")
        # secrets=[secret_env, secret_volume],
        # resources={'limit_memory': "250M", 'limit_cpu': "100m"},

    start >> [tap_cryptodata]
