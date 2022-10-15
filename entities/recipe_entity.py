from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, ForeignKey, Integer, String

from entities import base


class RecipeEntity(base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    protein = Column(Float)
    fats = Column(Float)
    carbohydrates = Column(Float)
    calories = Column(Float)
    logo_link = Column(String)
    products = relationship("RecipeProductEntity", backref='recipes', cascade="all, delete")


class RecipeProductEntity(base):
    __tablename__ = 'recipes_products'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
