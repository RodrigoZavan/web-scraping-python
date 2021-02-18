from urllib.request import  urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import pandas as pd

names_list = [] #Lista auxiliar
price_list = [] #Lista auxiliar
links_list = [] #Lista auxiliar

def getHTML(url): #Função que retorna o HTML da página
    try:
        url = urlopen(url)
    except HTTPError as e:
        print(f'HTTP error: {e}')   
    bs = BeautifulSoup(url, features='html.parser')
    return bs

url = 'https://loja.mercadolivre.com.br/tplink' #Link que será realizado a extração
html = getHTML(url)

name_elements = html.find_all('h2', {'class':'ui-search-item__title ui-search-item__group__element'}) #Elemento dos nomes
price_elements = html.find_all('div', {'class':'ui-search-price ui-search-price--size-medium ui-search-item__group__element'}) #Elemento dos preços
links_elements = html.find_all('a', {'class':'ui-search-result__content ui-search-link'}, href=True) #Elemento dos links

for name in name_elements: #Loop que extrai os nomes e armazena na lista auxiliar
    names_list.append(name.text)

for price in price_elements: #Loop que extrai os preços e armazena na lista auxiliar
    price_list.append(price.text)

for link in links_elements: #Loop que extrai os links e armazena na lista auxiliar
    links_list.append(link['href'])

dados = {'Item':names_list, #Transforma as listas em um dicionário
        'Preco':price_list,
        'Link':links_list}

df = pd.DataFrame(data=dados) #Transforma as listas em um data frame

df.to_csv('df.csv', sep=";", encoding="utf-8", index=False) #Exporta os dados em um arquivo csv