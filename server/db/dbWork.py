import sqlalchemy
from databases import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///test.db"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)

inbox = sqlalchemy.Table(
    "inbox",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("Code", sqlalchemy.Integer), 
    sqlalchemy.Column("fileName", sqlalchemy.String, unique=True), 
    sqlalchemy.Column("DateAndTime", sqlalchemy.String), 
)