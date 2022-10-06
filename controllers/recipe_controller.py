from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from services.sessions import generate_session

recipe_controller = APIRouter()


@recipe_controller.get("/api/recipes")
def get_recipes(ids: List[int] = Query(None, alias="ids"),
                session: Session = Depends(generate_session)):
    return ids
