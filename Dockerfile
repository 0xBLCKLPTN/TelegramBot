FROM python:3.8

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

EXPOSE 5432:5432

COPY requirements.txt .
COPY . .
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

