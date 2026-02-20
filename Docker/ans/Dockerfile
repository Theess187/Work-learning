FROM ubuntu:22.04
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    curl \
    unzip \
    wget \
    libssl-dev \
    libcurl4-openssl-dev \
    python3 \
    python3-venv \
    python3-pip 
WORKDIR /ansible
COPY /ans .
