from bs4 import BeautifulSoup
import requests
from sqlalchemy.orm import Session
from tqdm import tqdm
import colorama
from entities.product_entity import ProductEntity
from entities.recipe_entity import RecipeEntity, RecipeProductEntity
from services.product_service import get_products_by_name
from services.sessions import generate_session


def get_recipe_products(html, session) -> list[ProductModel]:
    bs = BeautifulSoup(html, "html.parser")
    ing_block = bs.find('div', class_="field field-type-text recipes-ingredients")
    prods_li = ing_block.find_all('li', class_='recipes-ingr-item')
    products_names = [' '.join(prod.text.split()[:-3]) for prod in prods_li]
    prod_models = [get_products_by_name(n, session)[0] for n in products_names]

    return prod_models


calorizator_url = 'https://calorizator.ru'


def parse():
    session: Session = next(generate_session())

    for i in range(88)[:1]:
        url = f"{calorizator_url}/recipes/all?page={i}"
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        table = soup.find('tbody')

        trs = table.find_all('tr')
        for tr in trs[:1]:
            cols = tr.find_all("td")
            name, protein, fat, carb, kal = get_data_from_html_table(cols)
            href = cols[1].a['href']
            products = get_recipe_products(requests.get(calorizator_url + href).text, session)
