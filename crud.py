from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_email: str):
    db_item = models.Item(**item.dict(), owner_email=user_email)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


class OnlineSlaCrud:
    def __init__(self):
        self.session = SessionLocal()

    def read_online_data(
        self,
            page:int=1,
            limit: int = 10,
    ):
        query = (
            self.session.query(models.User)
            .join(models.Item)
            .filter(models.Item.owner_email == models.User.email)
        )
        total = query.count()
        return query.offset((page - 1) * limit).limit(limit).all(), page, limit, total
