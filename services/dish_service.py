from typing import List

from sqlalchemy.orm import Session

from entities.product_entity import ProductEntity
from services import product_service


def get_dishes(product_names: List[str], session: Session):
    dishes = []
    for product_name in product_names:
        product: ProductEntity = product_service.get_product_by_name(product_name, session)
        dishes += product.recipes
    return dishes
