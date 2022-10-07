from typing import List

from sqlalchemy.orm import Session

from entities.category_entity import CategoryEntity
from entities.product_entity import ProductEntity


def add_category(name: str, session: Session):
    category = CategoryEntity()
    category.name = name
    session.add(category)
    session.commit()


def is_category_exist(name, session: Session):
    return session.query(CategoryEntity).filter_by(name=name).first() is not None


def add_category_to_product(category: str, product: ProductEntity, session: Session):
    category_entity: CategoryEntity = get_category_by_name(category, session)
    if category_entity.id != product.category:
        category_entity.products.append(product)
    session.commit()


def get_category_by_name(name: str, session: Session):
    return session.query(CategoryEntity).filter_by(name=name).first()
