import bs4
import requests
from bs4 import BeautifulSoup
import requests as req
from sqlalchemy.orm import Session
from tqdm import tqdm
import colorama

from entities.product_entity import ProductEntity
from services import category_service, product_service
from services.product_service import is_database_empty
from services.sessions import generate_session
from models.product_model import ProductModel

colorama.init()


def main():
    session: Session = next(generate_session())
    if not is_database_empty(session):
        print(colorama.Fore.RED, "DATABASE IS NOT EMPTY!!!", colorama.Fore.RESET)
        return

    for i in tqdm(range(80)):
        url = f"https://calorizator.ru/product/all?page={i}"

        soup = BeautifulSoup(req.get(url).text, "html.parser")

        tbody = soup.find('tbody')
        rows = tbody.find_all("tr")

        for row in rows:
            row: bs4.Tag
            cols = row.find_all("td")
            name = cols[1].text.strip() + " "
            product_link = cols[1].contents[1].attrs["href"]
            category = get_product_category(product_link, session)
            protein = float(cols[2].text.strip() if cols[2].text.strip() != "" else 0)
            fat = float(cols[3].text.strip() if cols[3].text.strip() != "" else 0)
            carb = float(cols[4].text.strip() if cols[4].text.strip() != "" else 0)
            kal = float(cols[5].text.strip() if cols[5].text.strip() != "" else 0)
            product_model = ProductModel(name=name, protein=protein, fats=fat, carbohydrates=carb, calories=kal)
            product = ProductEntity(**product_model.__dict__)
            data = product_service.get_products_by_name(product.name, session)
            if not data:
                category_service.add_category_to_product(category, product, session)
                session.add(product)
    session.commit()


def get_product_category(link: str, session: Session):
    url = f"https://calorizator.ru{link}"
    resp = requests.get(url)
    bs = BeautifulSoup(resp.text, "html.parser")
    categories = bs.find('div', class_="breadcrumb")
    category = categories.contents[4].text
    if not category_service.is_category_exist(category, session):
        category_service.add_category(category, session)
    return category
