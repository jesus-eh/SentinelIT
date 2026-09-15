from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


engine = create_engine(settings.DATABASE_URL)

Session = sessionmaker(bind=engine)

# session = Session()

def get_db():
    
    return Session()