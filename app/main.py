from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from .models import Base
from . import schemas, crud

app = FastAPI()

print("Applied Migration to the Database")
Base.metadata.create_all(bind=engine)


# dependency to get db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Annotated[Session, Depends(get_db)]):
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    return crud.get_user(db, user_id=user_id)