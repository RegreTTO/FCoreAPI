from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from services import dish_service
from services.sessions import generate_session

dish_controller = APIRouter()


@dish_controller.get("/api/dish")
def get_dishes(product_names: List[str] = Query(None, alias="names"),
               session: Session = Depends(generate_session)):
    return dish_service.get_dishes(product_names, session)
