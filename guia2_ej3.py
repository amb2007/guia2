import pyperclip, requests, webbrowser, sys
from bs4 import BeautifulSoup

def urls():
    sig= soup.find('a', {'class' : 'next'})
    url = sig.get('href')#consigo el href de el art
    return(url)
def arts(soup):
    lista.extend(soup.find_all('article'))#no se porque me devuelve que el soup es = a noneType
    return lista#consigo y devuelvo todos los articulos de la pag
cont = 0
paste = pyperclip.paste()
while True:
    folder = pyperclip.paste()
    if folder != paste :
        lista = []
        for cont in range(5):#bucle hasta 5
            data = requests.get(folder)
            soup = BeautifulSoup(data.text, 'html.parser')
            arts(soup)
            folder=urls()





