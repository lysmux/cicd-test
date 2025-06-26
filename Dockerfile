FROM python:3.13.0-slim-bullseye AS builder

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==2.1.2 \
    && poetry config virtualenvs.in-project true \
    && poetry install --only main --no-interaction --no-ansi

FROM python:3.13.0-slim-bullseye

WORKDIR /app

COPY --from=builder /app ./
COPY ./app ./app/

EXPOSE 80

ENTRYPOINT [".venv/bin/uvicorn", "--factory", "app.main:getapp", "--host", "0.0.0.0", "--port", "80"]