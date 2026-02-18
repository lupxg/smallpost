import os
from typing import List, Type

def read_secret(path):
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def build_db_url():
    password = read_secret("/run/secrets/db-password")
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    name = os.getenv("DB_NAME")
    port = os.getenv("DB_PORT")

    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}"


class Config:
    SECRET_KEY = 'JGAA9GA9AGHUAGJAKGJAGjgakl7ga7u'


class DevelopmentConfig(Config):
    CONFIG_NAME = "development"
    DEBUG = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_recycle": 200,
        "pool_pre_ping": True,
    }
    TESTING = True
    SQLALCHEMY_DATABASE_URI = build_db_url()


class ProductionConfig(Config):
    CONFIG_NAME = "production"
    DEBUG = False
    TESTING = False


EXPORT_CONFIGS: List[type[Config]] = [
    DevelopmentConfig,
    ProductionConfig,
]

config_by_name= {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}