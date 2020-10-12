FROM python:3.9.0-alpine as base

ENV PYTHONUNBUFFERED 1

# ----

FROM base as builder

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev

RUN python -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY requirements/prod.txt requirements.txt

RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

# ----

FROM base

RUN apk update && apk add --no-cache \
    libpq

RUN adduser -D -u 1000 appuser

USER appuser

WORKDIR /home/appuser/project

COPY --from=builder /venv /venv

ENV PATH="/venv/bin:$PATH"

COPY . .

EXPOSE 8000

CMD gunicorn \
    --workers=$((2 * $(getconf _NPROCESSORS_ONLN) + 1)) \
    --bind 0.0.0.0:8000 \
    server.wsgi:application
