FROM ubuntu:latest

RUN apt update
RUN apt install -y ffmpeg python3 python3-pip


RUN pip3 install -U flask
RUN pip3 install -U setuptools-rust
RUN pip3 install -U openai-whisper
RUN pip3 install -U uuid

RUN mkdir -p /svc/uploads
WORKDIR /svc

COPY src/app.py /svc
COPY entrypoint.sh /

ENTRYPOINT entrypoint.sh

