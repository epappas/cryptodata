FROM apache/airflow:2.0.1-python3.7

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    libpq-dev gcc python3.7-dev \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow

# ADD ./plugins /opt/airflow/plugins
ADD ./lib /opt/airflow/lib
ADD requirements.txt /opt/airflow/requirements.txt

RUN pip install --ignore-installed \
  --no-cache-dir --user --upgrade \
  --upgrade-strategy only-if-needed \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.0.1/constraints-3.7.txt" \
  -r requirements.txt
