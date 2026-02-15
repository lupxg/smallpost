# syntax=docker/dockerfile:1

# BASE
FROM python:3.13.3-slim-bookworm AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



# DEVELOPMENT
FROM base AS dev

ENV FLASK_ENV=development
ENV FLASK_APP=app.py

COPY . .

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]



# PRODUCTION
FROM base AS prod

RUN pip --no-cache-dir install gunicorn

COPY . .

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]