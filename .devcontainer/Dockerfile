FROM python:3.13.1-slim-bullseye


RUN apt-get update \
    && apt-get -y install tesseract-ocr \
    && apt-get -y install wget \
# cleanup
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/\* /tmp/\* /var/tmp/* 