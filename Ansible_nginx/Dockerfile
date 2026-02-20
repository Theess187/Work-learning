FROM ubuntu:22.04
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    python3 \
    python3-venv \
    python3-pip \
    net-tools\
    iputils-ping
RUN apt-get install -y sshpass
RUN pip3 install ansible
ENV ANSIBLE_HOST_KEY_CHECKING=False
WORKDIR /ansible
COPY /ans .

