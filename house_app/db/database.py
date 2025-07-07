from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL = 'postgresql://postgres:adminadmin@localhost/house_app'
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()