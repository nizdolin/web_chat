FROM python:3.13-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
ENV PATH="/root/.local/bin:$PATH"
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev

COPY ./app ./app
