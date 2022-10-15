from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from entities import base


class CategoryEntity(base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("ProductEntity", cascade="all, delete", backref="recipe")
