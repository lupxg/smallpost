# syntax=docker/dockerfile:1

FROM python:3.13.3-slim-bookworm AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:4000", "app:app"]