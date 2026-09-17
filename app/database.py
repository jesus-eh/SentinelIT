from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(settings.DB_URL)

Session = sessionmaker(bind=engine)

# session = Session()

def get_db():
    return Session()