FROM python:3.9.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache \
    gcc \
    libpq \
    musl-dev \
    postgresql-dev

WORKDIR /app/project

COPY requirements/dev.txt requirements.txt

RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
