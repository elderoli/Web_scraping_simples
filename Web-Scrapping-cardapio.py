import requests
from bs4 import BeautifulSoup

page = requests.get("https://cardapiodemao.com/exemplo.html")

soup = BeautifulSoup(page.content, "lxml")

titulo_tags = soup.find_all('div', class_='shop-item')
preco_tags = soup.find_all('span', class_='shop-item-price')
for titulo in titulo_tags:
    titulo_ = titulo.span.text

    for preco in preco_tags:
        preco_ = preco.text


    print(titulo_)
    print(preco_)
