from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(64), unique=True, index=True)
    hashed_password = Column(String(64))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

    def __repr__(self):
        return f"<User>:email:{self.email}"


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), index=True)
    description = Column(String(64), index=True)
    owner_email = Column(String(64), ForeignKey("users.email"))

    owner = relationship("User", back_populates="items")

    def __repr__(self):
        return f"<Item>:ForeignKey:{self.owner_email}, {self.title}"
