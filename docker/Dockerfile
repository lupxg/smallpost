FROM python:3.14.2-slim-trixie AS base 

WORKDIR /app 

ARG APP_UID=1000 
ARG APP_GID=1000 

RUN apt-get update \ 
    && apt-get install -y --no-install-recommends curl \ 
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \ 
    && apt-get clean \ && groupadd -g "${APP_GID}" appuser \ 
    && useradd --create-home --no-log-init -u "${APP_UID}" -g "${APP_GID}" appuser \ 
    && chown appuser:appuser -R /app 
    
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

USER appuser 

COPY --chown=appuser:appuser pyproject.toml uv.lock* . 

ENV PYTHONDONTWRITEBYTECODE=1 \ 
    PYTHONUNBUFFERED=1 \ 
    UV_COMPILE_BYTECODE=1 \ 
    UV_LINK_MODE=copy \ 
    UV_PROJECT_ENVIRONMENT="/home/appuser/.local" \ 
    UV_PYTHON=python3.14 \ 
    PATH="${PATH}:/home/appuser/.local/bin" \ 
    USER="appuser" 

RUN --mount=type=cache,target=/app/.cache/uv \ 
    uv sync --frozen --no-install-project 
    
CMD ["bash"] 

########################################################################################## 

# DEVELOPMENT 

FROM base AS dev 

COPY --chown=appuser:appuser . . 

RUN --mount=type=cache,target=/app/.cache/uv \ 
    uv sync --frozen 


EXPOSE 8000 
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app.app:app"]