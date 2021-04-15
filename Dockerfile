FROM apache/airflow:2.0.1-python3.7

ADD requirements.txt /opt/airflow/requirements.txt

RUN pip install --ignore-installed \
  --no-cache-dir --user --upgrade \
  --upgrade-strategy only-if-needed \
  -r requirements.txt
