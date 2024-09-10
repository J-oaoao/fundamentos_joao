import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=Jo%C3%A3o+Felipe&"
requisicao = requests.get(link)
print(requisicao)
# print(requisicao.text)
site = BeautifulSoup (requisicao.text, "html.parser")
# print(site.prettify())

# mais simples print(site.title)
# mais preciso titulo = site.find("title") ^ print(titulo)
input = site.find_all("input")
print(input)
