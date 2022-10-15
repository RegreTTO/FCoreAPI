from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from entities import base


class ProductEntity(base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    protein = Column(Float)
    fats = Column(Float)
    carbohydrates = Column(Float)
    calories = Column(Float)
    category = Column(Integer, ForeignKey("categories.id"))
    recipes = relationship("RecipeProductEntity", backref="products", cascade="all, delete")
