
import requests
from bs4 import BeautifulSoup



#link do site com as ultimas noticias do povo
link = "https://www.opovo.com.br/noticias/checagemopovo/"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

# identificamos a lista com todas as noticias da pagina
noticias = soup.find("div", class_="container container-listagem").find("div", class_="listagem")


for i in noticias.find_all("div"):
    try:

        #selecionamos o link da noticia da pagina inicial
        page = requests.get(i.a.attrs['href'])
        soup = BeautifulSoup(page.content, 'html.parser')

        #coleta dos valores da noticia

        titulo = soup.find("h1", class_="titulo")
        subtitulo = soup.find("span", class_="subtitulo")
        informacoes = soup.find("div", class_="caixa-status")

        Autor = informacoes.div.span.text
        Horario_Publicacao = informacoes.span.text
        Textos = ''

        for textos in soup.find_all("p",class_="texto"):
            Textos += textos.text + " "

        print([titulo.text,subtitulo.text,Autor,Horario_Publicacao,Textos])

    #Apos a coleta, é necessario adicionar uma estrutura para guardar os coletados, seja um json, csv ou banco de dados

    except:
        aux = 0