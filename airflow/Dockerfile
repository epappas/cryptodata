FROM apache/airflow:2.0.1-python3.7

ARG MELTANO_PYPI="meltano"
ARG MELTANO_VERSION="1.71.0"

USER root

ENV VIRTUAL_ENV=/opt/venv/meltano
RUN mkdir -p /opt/venv/
RUN python3 -m venv $VIRTUAL_ENV

RUN . $VIRTUAL_ENV/bin/activate && \
  pip install --ignore-installed \
  --no-cache-dir --upgrade \
  --upgrade-strategy only-if-needed \
  meltano==$MELTANO_VERSION

USER airflow

ADD requirements.txt /opt/airflow/requirements.txt

RUN pip install --ignore-installed \
  --no-cache-dir --user --upgrade \
  --upgrade-strategy only-if-needed \
  -r requirements.txt
