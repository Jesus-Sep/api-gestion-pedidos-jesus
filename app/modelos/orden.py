from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status_id = Column(Integer, ForeignKey("order_statuses.id"), nullable=False)

    user = relationship("User", back_populates="orders")
    status = relationship("OrderStatus")
    items = relationship("OrderItem", back_populates="order")
