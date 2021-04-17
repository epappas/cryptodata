# base image
FROM apache/superset:1.1.0

ADD ./docker /app/docker
ADD requirements.txt /app/docker/requirements.txt

USER root
RUN pip install --ignore-installed \
  --no-cache-dir --user --upgrade \
  --upgrade-strategy only-if-needed \
  -r /app/docker/requirements.txt

USER superset
