import os

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

    return f"mysql+pymysql://{user}:{password}@{host}:3306/{name}"


class Config:
    SECRET_KEY = 'JGAA9GA9AGHUAGJAKGJAGjgakl7ga7u'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_recycle": 200,
        "pool_pre_ping": True,
    }
    SQLALCHEMY_DATABASE_URI = build_db_url()
class ProductionConfig(Config):
    DEBUG = False