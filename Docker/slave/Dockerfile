FROM ubuntu:22.04
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    net-tools\
    iputils-ping
WORKDIR /app
COPY . .