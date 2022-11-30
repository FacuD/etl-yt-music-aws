from cfg import DB_CONNSTR
from constants import TABLENAME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    create_engine,
    Integer,
    Column,
    String,
    DateTime,
)

engine = create_engine(DB_CONNSTR)
Base = declarative_base()


class History(Base):
    __tablename__ = TABLENAME
    id = Column(Integer, primary_key=True, autoincrement=True)
    song_id = Column(String(255))
    title = Column(String(100), nullable=False)
    artist = Column(String(100), nullable=False)
    played_at = Column(String(50), nullable=False)
    inserted_at = Column(DateTime(timezone=True), server_default=func.now())


Session = sessionmaker(engine)
session = Session()


def create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def upload_songs(songs_df):
    try:
        with engine.begin() as conn:
            songs_df.to_sql(TABLENAME, conn, index=False, if_exists="append")
            print("Songs uploaded succesfully")
    except Exception as e:
        print(
            "Some songs were not uploaded"
        )
        print(f"Error: {e}")
