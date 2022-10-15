from typing import List

from pydantic import BaseModel

from entities.product_entity import ProductEntity
from entities.recipe_entity import RecipeEntity


class ProductRecipeModel(BaseModel):
    products: list
    recipes: list
    

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

