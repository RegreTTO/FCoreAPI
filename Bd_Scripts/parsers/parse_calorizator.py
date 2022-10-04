from bs4 import BeautifulSoup
import requests
from services.products import get_product
from Bd_Scripts import get_data_from_html_table
from models.product_model import ProductModel


def get_recipe_products(html) -> list[ProductModel]:
    bs = BeautifulSoup(html)
    return get_product("ads")


calorizator_url = 'https://calorizator.ru'

for i in range(88)[:1]:
    url = f"{calorizator_url}/recipes/all?page={i}"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    table = soup.find('tbody')

    trs = table.find_all('tr')
    for tr in trs[:1]:
        cols = tr.find_all("td")
        name, protein, fat, carb, kal = get_data_from_html_table(cols)
        href = cols[1].a['href']
        products = get_recipe_products(requests.get(calorizator_url + href).text)
