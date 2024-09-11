import requests
from bs4 import BeautifulSoup

link = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
#headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

requisicao = requests.get(link)
print(requisicao)

site = BeautifulSoup (requisicao.text, "html.parser")
# print(site.prettify())

titulo = site.find_all("a")
print(titulo)

pesquisa2 = site.find("a", class_="row")
print(pesquisa2)
