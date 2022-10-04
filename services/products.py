from sqlalchemy.orm import Session, Query

from entities.product_entity import ProductEntity
from services.sessions import generate_session

session: Session = next(generate_session())


def get_product(product_name: str):
    req: Query = session.query(ProductEntity).filter_by(name=product_name)
    prod = req.one()
    if prod is not None:
        return prod
    raise ValueError("Product not found")
