from urllib.request import  urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import pandas as pd

names_list = []
price_list = []
links_list = []

def getHTML(url):
    try:
        url = urlopen(url)
    except HTTPError as e:
        print(f'HTTP error: {e}')   
    bs = BeautifulSoup(url, features='html.parser')
    return bs

url = 'https://loja.mercadolivre.com.br/tplink'
html = getHTML(url)

name_elements = html.find_all('h2', {'class':'ui-search-item__title ui-search-item__group__element'})
price_elements = html.find_all('div', {'class':'ui-search-price ui-search-price--size-medium ui-search-item__group__element'})
links_elements = html.find_all('a', {'class':'ui-search-result__content ui-search-link'}, href=True)

for name in name_elements:
    names_list.append(name.text)

for price in price_elements:
    price_list.append(price.text)

for link in links_elements:
    links_list.append(link['href'])

dados = {'Item':names_list,
        'Preco':price_list,
        'Link':links_list}

df = pd.DataFrame(data=dados)

df.to_csv('df.csv', sep=";", encoding="utf-8", index=False)