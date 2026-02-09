from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

    role = relationship("Role")
    orders = relationship("Order", back_populates="user")
