from pydantic import BaseModel


class ProductRecipeModel(BaseModel):
    products: list
    recipes: list

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
