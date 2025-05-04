FROM python:3.12-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential ffmpeg pkg-config libgl1-mesa-glx libsm6 \
    && pip install --no-cache-dir --upgrade pip \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --requirement /app/requirements.txt

COPY . /app

#No port exposed because its not a service to request but just a consumer
CMD [ "python3", "consumer.py"]


