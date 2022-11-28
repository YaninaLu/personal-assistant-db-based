from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///contacts.db", echo=True)
DB_session = sessionmaker(bind=engine)
session = DB_session()
