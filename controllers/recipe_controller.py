from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from services import recipe_service
from services.sessions import generate_session

recipe_controller = APIRouter()


@recipe_controller.get("/api/recipes")
def get_recipes(ids: List[int] = Query(None, alias="ids"),
                session: Session = Depends(generate_session)):
    return ids


@recipe_controller.get("/api/dish/recipe")
def get_dish_recipe(product_names: List[str] = Query(None, alias="names"),
                    session: Session = Depends(generate_session)):
    return recipe_service.get_dish(product_names, session)
