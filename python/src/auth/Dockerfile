FROM python:3.12-slim-bullseye

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends --no-install-suggests \
#     build-essential default-libmysqlclient-dev \
#     && pip install --no-cache-dir --upgrade pip 

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libmariadb-dev \
    && pip install --no-cache-dir --upgrade pip \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --requirement /app/requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "python3", "server.py"]


