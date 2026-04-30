# syntax=docker/dockerfile:1

## -----------------------------------------------------
## Build stage (use tag with -dev suffix: e.g. 3.9.23-debian13-fips-dev)
FROM dhi.io/python:3-debian13-sfw-ent-dev  AS build-stage

RUN apt-get update
RUN apt-get install -y procps vim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app

RUN python -m venv /app/venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "/app/app.py"]
