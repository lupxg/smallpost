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

COPY . .

EXPOSE 5000
CMD ["python","app.py"]



# PRODUCTION
FROM base AS prod

RUN pip --no-cache-dir install gunicorn

COPY . .

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]