from app.config import build_db_url
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(build_db_url())
Base = declarative_base()
Session = sessionmaker(bind=engine)


def create_tables():
    from app.posts.model import Post
    
    Base.metadata.create_all(engine)