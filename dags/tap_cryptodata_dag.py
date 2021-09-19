"""An example DAG demonstrating Kubernetes Pod Operator."""

import datetime

from airflow import models
from kubernetes.client import models as k8s
from airflow.kubernetes.secret import Secret
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

configmaps = ['test-configmap-1', 'test-configmap-2']
port = k8s.V1ContainerPort(name='http', container_port=80)
secret_env = Secret(
    deploy_type='env',
    deploy_target='SQL_CONN',
    secret='airflow-secrets',
    key='sql_alchemy_conn')
secret_volume = Secret(
    deploy_type='volume',
    deploy_target='/var/secrets/google',
    secret='service-account',
    key='service-account.json')

volume = k8s.V1Volume(
    name='test-volume',
    persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(claim_name='test-volume'),
)
volume_mount = k8s.V1VolumeMount(
    name='test-volume', mount_path='/root/mount_file', sub_path=None, read_only=True
)

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
        dag=dag)
        # arguments=['{{ ds }}'],
        # env_vars={'MY_VALUE': '{{ var.value.my_value }}'},
        # config_file="{{ conf.get('core', 'kube_config') }}")
        # resources={'limit_memory': "250M", 'limit_cpu': "100m"},
        # ports=[port],
        # volumes=[volume],
        # volume_mounts=[volume_mount],
        # init_containers=[init_container],
        # affinity={},
        # volumes=[volume],
        # volume_mounts=[volume_mount],
        # secrets=[secret_env, secret_volume],
        # configmaps=configmaps,

    start >> [tap_cryptodata]
