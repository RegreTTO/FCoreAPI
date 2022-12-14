from typing import Optional
from urllib.parse import unquote

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.sessions import generate_session
from services import product_service

product_controller = APIRouter()


@product_controller.get("/api/products")
def get_products(limit: Optional[int] = -1, session: Session = Depends(generate_session)):
    return product_service.get_products(limit=limit, session=session)


@product_controller.get("/api/product/{product_id}")
def get_product(product_id: int, session: Session = Depends(generate_session)):
    return product_service.get_product(product_id, session)


@product_controller.get("/api/product/name/{product_name}")
def get_product_by_name(product_name: str, session: Session = Depends(generate_session)):
    n = unquote(product_name.lower())
    return product_service.get_products_by_name(n, session)
