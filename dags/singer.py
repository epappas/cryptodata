from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'robertjmoore',
    # 'depends_on_past': True,
    'start_date': datetime(2016, 7, 13),
    'email': ['robertj@robertjmoore.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'singer-sync', default_args=default_args, schedule_interval=timedelta(1))

t_singertest = BashOperator(
    task_id='singer_test',
    bash_command='tap-git',
    retries=1,
    dag=dag)
