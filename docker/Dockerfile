# syntax=docker/dockerfile:1

FROM python:3.13.3-slim-bookworm AS builder
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Using base flask CLI tool to run the server.
FROM builder AS development
COPY . .
EXPOSE 5000
CMD ["flask", "run"]

#Using gunicorn
FROM builder AS production
RUN pip install gunicorn
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:4000", "app:app"]