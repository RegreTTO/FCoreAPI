from pydantic import BaseModel
from entities.recipe_entity import RecipeEntity


class RecipeGetModel(BaseModel):
    id: int
    name: str
    protein: float
    fats: float
    carbohydrates:  float
    calories:  float

    @staticmethod
    def to_model(recipe: RecipeEntity):
        model = RecipeGetModel(
            id=recipe.id,
            name=recipe.name,
            protein=recipe.protein,
            fats=recipe.fats,
            carbohydrates=recipe.carbohydrates,
            calories=recipe.calories
        )
        return model

