from bs4 import BeautifulSoup
import httpx

# Função para acessar a página
def acessar_pagina(url):
    """Acessa uma URL e retorna o BeautifulSoup e o código de status."""
    try:
        resposta = httpx.get(url)
        resposta.raise_for_status()
        soup = BeautifulSoup(resposta.text, "html.parser")
        return soup, resposta.status_code
    except httpx.RequestError as e:
        print(f"Erro ao acessar {url}: {e}")
        return None, None


# Função para extrair informações da página principal
def extrair_infos_principais(soup):
    """Extrai o título da página principal."""
    if soup:
        titulo = soup.find("h1")
        if titulo:
            print(f"Título: {titulo.text.strip()}")
        else:
            print("Título não encontrado na página principal.")
    else:
        print("Erro: Soup inválido na função extrair_infos_principais.")


# Função para acessar e processar as divs anuais
def acessar_e_processar_div_anuais(soup):
    """Extrai informações das divs anuais, removendo espaços em branco dos links."""
    if soup:
        divs_anuais = soup.find_all('div', class_='controle_conteudo')
        if divs_anuais:
            for div in divs_anuais:
                links = div.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href:
                        href_limpo = href.strip()
                        print(f"Link encontrado (limpo): {href_limpo}")
        else:
            print("Divs anuais não encontradas.")
    else:
        print("Erro: Soup inválido na função acessar_e_processar_div_anuais.")


# Função principal
def main():
    site_sen = 'https://www25.senado.leg.br/web/atividade/anais/anais-da-republica/-/republica/'
    lista_de_url_sen = [f'{site_sen}{contador}' for contador in range(48, 56)]

    for link in lista_de_url_sen:
        print(f"Processando: {link}")
        soup, status_code = acessar_pagina(link)

        if soup:
            extrair_infos_principais(soup)
            acessar_e_processar_div_anuais(soup)
        else:
            print(f"Erro ao acessar a página: {status_code}")

        print("===" * 10)


if __name__ == '__main__':
    main()