from bs4 import BeautifulSoup
import requests
from sqlalchemy.orm import Session
from tqdm import tqdm

from entities.product_entity import ProductEntity
from entities.recipe_entity import RecipeEntity, RecipeProductEntity
from services.product_service import get_products_by_name
from services.sessions import generate_session


def get_recipe_products(html, session) -> list:
    bs = BeautifulSoup(html, "html.parser")
    ing_block = bs.find('div', class_="field field-type-text recipes-ingredients")
    prods_li = ing_block.find_all('li', class_='recipes-ingr-item')
    products_names = [' '.join(prod.text.split()[:-2]) for prod in prods_li]
    products_models = []
    for name in products_names:
        models = get_products_by_name(name, session)
        if models:
            products_models.append(models[0])

    return products_models


calorizator_url = 'https://calorizator.ru'


def parse():
    session: Session = next(generate_session())

    for i in tqdm(range(88)):
        url = f"{calorizator_url}/recipes/all?page={i}"
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        table = soup.find('tbody')

        trs = table.find_all('tr')

        for tr in trs:
            cols = tr.find_all("td")
            image_url = cols[0].a['href']
            name = cols[1].text.strip().lower()
            protein = float(cols[2].text.strip() if cols[2].text.strip() != "" else 0)
            fat = float(cols[3].text.strip() if cols[3].text.strip() != "" else 0)
            carb = float(cols[4].text.strip() if cols[4].text.strip() != "" else 0)
            kal = float(cols[5].text.strip() if cols[5].text.strip() != "" else 0)
            href = cols[1].a['href']
            products: set[ProductEntity] = set(get_recipe_products(requests.get(calorizator_url + href).text, session))
            products = set(filter(lambda x: x != [], products))
            recipe = RecipeEntity(name=name, protein=protein, fats=fat, carbohydrates=carb, calories=kal,
                                  logo_link=image_url)
            session.add(recipe)
            session.commit()
            for prod in products:
                link_row = RecipeProductEntity(product_id=prod.id, recipe_id=recipe.id)
                session.add(link_row)
    session.commit()
