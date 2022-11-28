from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime

from db_session import engine


Base = declarative_base()

notes_tags_conn = Table(
    "notes_to_tags",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("note", Integer, ForeignKey("notes.id")),
    Column("tag", Integer, ForeignKey("tags.id")),
)


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    birthday = Column(DateTime)
    email = Column(String(50), unique=True)
    phone = Column(String(20), unique=True)
    address = Column(String(70))


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False, unique=True)
    created_on = Column(DateTime, default=datetime.now())
    text = Column(String(500), nullable=False)
    tags = relationship("Tag", secondary=notes_tags_conn, backref="notes")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)


Base.metadata.create_all(engine)
Base.metadata.bind = engine
