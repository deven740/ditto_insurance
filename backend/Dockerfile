FROM python:3.10
RUN apt-get update
RUN apt-get install
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .