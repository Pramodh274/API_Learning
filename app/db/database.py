from sqlalchemy import create_engine, MetaData
from databases import Database

# Database URL for SQLite
DATABASE_URL = "sqlite:///./test.db"

# Create a SQLAlchemy engine and metadata object
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()

# Create a Database instance for async operations
database = Database(DATABASE_URL)
