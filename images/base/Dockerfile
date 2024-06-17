FROM ubuntu:20.04

WORKDIR /root

RUN apt-get update \
    && apt-get install -y python3 python3-venv python3-pip

RUN pip3 install --upgrade pip setuptools wheel
