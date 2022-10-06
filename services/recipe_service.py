from typing import List

from sqlalchemy.orm import Session

from entities.recipe_entity import RecipeEntity


def get_recipes_by_id(ids: List[int], session: Session):
    return get_recipes(ids, session)


def get_recipes(ids: List[int], session: Session):
    recipes = []
    for id in ids:
        recipe = get_recipe(id, session)
        if not recipe:
            continue
        recipes.append(recipe)
    return recipes


def get_recipe(id: int, session: Session) -> RecipeEntity:
    return session.query(RecipeEntity).filter_by(id=id).first()
