from bs4 import BeautifulSoup
import requests

url = 'https://labriunesp.org/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())