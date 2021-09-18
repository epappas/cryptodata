FROM apache/airflow:2.1.2-python3.8

RUN pip install --upgrade pip
RUN pip install -U pip setuptools==58.0.1 wheel

# Should have added this, but airflow has not managed their dependencies right.
# --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.15/constraints-3.7.txt" \

ADD requirements.txt /opt/airflow/requirements.txt
RUN pip install --ignore-installed \
  --no-cache-dir --user --upgrade \
  --upgrade-strategy only-if-needed \
  -r /opt/airflow/requirements.txt

ADD scripts /opt/airflow/scripts
ADD dags /opt/airflow/dags
ADD appconfig /opt/airflow/appconfig
ADD tests /opt/airflow/tests
