from sqlalchemy.orm import relationship

from entities import base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class RecipeEntity(base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("RecipeProductEntity", backref='recipe')


class RecipeProductEntity(base):
    __tablename__ = 'recipes_products'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
