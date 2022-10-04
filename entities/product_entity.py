from sqlalchemy import Column, Integer, String, Float
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
    recipes = relationship("RecipeProductEntity", backref="product")
