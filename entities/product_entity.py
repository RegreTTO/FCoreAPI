from sqlalchemy import Column, Integer, String, Float, ForeignKey

from entities.category_entity import CategoryEntity
from entities.recipe_entity import RecipeProductEntity
from entities import base
from sqlalchemy.orm import relationship


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
