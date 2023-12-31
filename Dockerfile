FROM ubuntu:latest

RUN apt update
RUN apt install -y ffmpeg python3 python3-pip

# The installations are folded out into multiple lines to take advantage of dockers
# layer caching. Eventually this should be refactored into its own file (requirements.txt)
RUN pip3 install -U flask
RUN pip3 install -U setuptools-rust
RUN pip3 install -U numpy
RUN pip3 install -U uuid
RUN pip3 install -U triton
RUN pip3 install -U cmake
RUN pip3 install -U torch
RUN pip3 install -U filelock
RUN pip3 install -U openai-whisper
RUN pip3 install -U uuid
RUN mkdir -p /svc/uploads

ARG WHISPER_MODEL="base"
ENV WHISPER_MODEL=${WHISPER_MODEL}

WORKDIR /svc

COPY src/download_model.py /svc/
# download model
RUN python3 /svc/download_model.py


COPY src/app.py /svc
COPY entrypoint.sh /

EXPOSE 5000

ENTRYPOINT /entrypoint.sh

