from pydantic import BaseModel


class ProductModel(BaseModel):
    name: str
    protein: float
    fats: float
    carbohydrates: float
    calories: float

    class Config:
        orm_mode = True
