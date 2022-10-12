from typing import List

from sqlalchemy.orm import Session

from entities.product_entity import ProductEntity


def get_products(session: Session):
    return session.query(ProductEntity).all()


def get_product(product_id: int, session: Session) -> ProductEntity:
    return session.query(ProductEntity).filter_by(id=product_id).first()


def get_products_by_name(product_name: str, session: Session) -> List[ProductEntity]:
    data = session.query(ProductEntity).filter(ProductEntity.name.like(f"{product_name} %")).all()
    i = 0
    while not data:
        data = session.query(ProductEntity).filter(
            ProductEntity.name.like(f'%{product_name[:len(product_name) - i]} %')).all()
        i += 1
        if i == len(product_name):
            return []
    return data


def get_product_by_name(product_name: str, session: Session) -> ProductEntity:
    return session.query(ProductEntity).filter_by(name=product_name).first()


def is_database_empty(session: Session):
    products = session.query(ProductEntity).all()
    return not products
