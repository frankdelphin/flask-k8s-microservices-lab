FROM python:3.12-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential \
    pkg-config \
    && pip install --no-cache-dir --upgrade pip \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --requirement /app/requirements.txt

COPY . /app

EXPOSE 8080

CMD [ "python3", "server.py"]


