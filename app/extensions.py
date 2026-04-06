from app.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def create_tables():
    from app.posts.model import Post
    
    Base.metadata.create_all(engine)
