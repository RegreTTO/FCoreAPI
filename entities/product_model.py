from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.orm import declarative_base

base = declarative_base()


class ProductEntity(base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    protein = Column(Float)
    fats = Column(Float)
    carbohydrates = Column(Float)
    calories = Column(Float)
