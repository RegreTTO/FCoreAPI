from pydantic import BaseModel

from entities.recipe_entity import RecipeEntity


class RecipeGetModel(BaseModel):
    id: int
    name: str
    protein: float
    fats: float
    carbohydrates: float
    calories: float
    logo_link: str

    @staticmethod
    def to_model(recipe: RecipeEntity):
        model = RecipeGetModel(
            id=recipe.id,
            name=recipe.name,
            protein=recipe.protein,
            fats=recipe.fats,
            carbohydrates=recipe.carbohydrates,
            calories=recipe.calories,
            logo_link=recipe.logo_link
        )
        return model
