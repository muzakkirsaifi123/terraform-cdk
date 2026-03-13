FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Exposing unnecessary port
EXPOSE 5000

# Running as root (bad practice)
USER root

# Hardcoded environment variable
ENV
