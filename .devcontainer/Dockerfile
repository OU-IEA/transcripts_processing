FROM python:3.13.1-slim-bullseye as builder

# install basic tools
RUN apt-get update && apt-get install --no-install-recommends --yes \
    apt-transport-https \
    automake \
    ca-certificates \
    g++ \
    libleptonica-dev \
    libtool \
    libicu-dev \
    libpango1.0-dev \
    libcairo2-dev \
    make \
    pkg-config \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/\* /tmp/\* /var/tmp/* 

WORKDIR /src

RUN wget https://github.com/tesseract-ocr/tesseract/archive/refs/tags/5.5.0.tar.gz
RUN tar -zxvf 5.5.0.tar.gz
WORKDIR ./tesseract-5.5.0


RUN ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

RUN wget https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata
RUN mv *.traineddata /usr/local/share/tessdata