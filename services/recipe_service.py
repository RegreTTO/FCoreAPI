from typing import List

from sqlalchemy.orm import Session

from entities.recipe_entity import RecipeEntity
from models.ProductRecipeModel import ProductRecipeModel
from models.recipe_get_model import RecipeGetModel
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


def get_dish(product_names: List[str], session: Session):
    products_recipes_model = get_list_of_products_and_recipes_by_product_names(product_names, session)
    product_frequency = get_products_frequency_in_recipe(products_recipes_model)
    res = {}
    for key, value in sorted(product_frequency.items(), key=lambda item: item[1]):
        res[key] = value
    result_products = []
    for recipe_id in res.keys():
        result_products.append(RecipeGetModel.to_model(get_recipe(recipe_id, session)))
    return result_products


def get_list_of_products_and_recipes_by_product_names(product_names: List[str], session: Session) -> ProductRecipeModel:
    products = []
    recipes = []
    for product_name in product_names:
        product = product_service.get_product_by_name(product_name + " ", session)
        products.append(product)
        recipes += [recipe.recipes for recipe in product.recipes]
    return ProductRecipeModel(products=products, recipes=recipes)


def get_products_frequency_in_recipe(product_recipe_model: ProductRecipeModel):
    # КОСТЫЛЬ MUST BE FIXED
    product_frequency = {}
    for recipe_product in product_recipe_model.recipes:
        for product in product_recipe_model.products:
            for recipe_product2 in recipe_product.products:
                if product.id == recipe_product2.product_id:
                    if not product_frequency.get(recipe_product):
                        product_frequency[recipe_product.id] = 1
                        continue
                    product_frequency[recipe_product.id] += 1
    return product_frequency
