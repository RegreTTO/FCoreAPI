import bs4
from bs4 import BeautifulSoup
import requests as req
from sqlalchemy.orm import Session
from tqdm import tqdm

from entities.product_model import ProductEntity
from models.product_model import ProductModel
from services.sessions import generate_session

products = []
session: Session = next(generate_session())
for i in tqdm(range(80)):
    url = f"https://calorizator.ru/product/all?page={i}"

    soup = BeautifulSoup(req.get(url).text, "html.parser")

    tbody = soup.find('tbody')
    rows = tbody.find_all("tr")
    for row in rows:
        row: bs4.Tag
        cols = row.find_all("td")
        name = cols[1].text.strip()
        protein = float(cols[2].text.strip() if cols[2].text.strip() != "" else 0)
        fat = float(cols[3].text.strip() if cols[3].text.strip() != "" else 0)
        carb = float(cols[4].text.strip() if cols[4].text.strip() != "" else 0)
        kal = float(cols[5].text.strip() if cols[5].text.strip() != "" else 0)
        product_model = ProductModel(name=name, protein=protein, fats=fat, carbohydrates=carb, calories=kal)
        product = ProductEntity(**product_model.__dict__)
        session.add(product)
session.commit()
print()
