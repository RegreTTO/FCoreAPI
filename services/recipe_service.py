from typing import List

from sqlalchemy.orm import Session

from entities.product_entity import ProductEntity
from entities.recipe_entity import RecipeEntity
from services import product_service


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


def get_dish_recipe(product_names: List[str], session: Session):
    products = generate_entity_list(product_names, session)
    products_ids = [prod.id for prod in products]
    recipes = [session.query(RecipeEntity).filter_by(id=5).first()]
    available_recipes = []
    for recipe in recipes:
        flags = []
        recipe_products_ids = [prod.product_id for prod in recipe.products]

        if all([prod_id in recipe_products_ids for prod_id in products_ids]):
            available_recipes.append(recipe)
    return available_recipes


def generate_entity_list(product_names: List[str], session: Session):
    products = []
    for name in product_names:
        products.append(product_service.get_product_by_name(name, session))
    return products


def get_all_recipes(session: Session):
    return session.query(RecipeEntity).all()
