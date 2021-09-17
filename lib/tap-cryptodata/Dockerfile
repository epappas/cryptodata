FROM python:3.8-slim-buster AS base

RUN apt-get update -y  \
 && apt-get upgrade -y \
 && apt-get install -y make gcc git ca-certificates python-pip python-dev libffi-dev libssl-dev \
 && pip install --upgrade pip

RUN pip install --upgrade pip
RUN pip install -U pip setuptools==58.0.1 wheel

FROM base

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN python -m pip install -r requirements.txt
RUN python -m pip install -e .

ENTRYPOINT ["tap-cryptodata"]
