from icecream import ic

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql://postgres@127.0.0.1/mastering_sqlalchemy"

# this doesn't open the connection immediately but prepares the connection setups
engine = create_engine(DATABASE_URL) 

# a session is use to handle transactions and communicatino with the database
# workspaces for queries and transactions
SessionLocal = sessionmaker(
    autocommit=False, # enforces manual commit of sql transactions
    autoflush=False, # 
    bind=engine
)

# this is base class which all our models would inherit from 
Base = declarative_base()