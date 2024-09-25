from bs4 import BeautifulSoup
import requests
#https://www25.senado.leg.br/web/atividade/anais/anais-da-republica/-/republica/48
site_sen = 'https://www25.senado.leg.br/web/atividade/anais/anais-da-republica/-/republica/'
pagina = requests.get(site_sen)
soup = BeautifulSoup(pagina.text, 'html.parser')
# print(soup)
# links = soup.find (attrs={'class': 'accordion-toggle collapsed'})
# anais = soup.find_all
lista_de_url_sen = []
contador = 48
while contador <= 56:
    url = f'{site_sen}{contador}'
    contador = contador + 1
    lista_de_url_sen.append(url)
#print(lista_de_url_sen)

for url in lista_de_url_sen:
    print(url)
    