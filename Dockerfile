FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYHONUNBUFFERED 1

WORKDIR /app

RUN apt update -y && \
    apt install -y python3-dev gcc musl-dev

ADD pyproject.toml /app
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi --without dev

COPY ./app /app
