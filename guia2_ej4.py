import pyperclip, requests, webbrowser, sys,os
from bs4 import BeautifulSoup

paste = pyperclip.paste()

while True:
    folder = pyperclip.paste()
    if folder != paste :
        print(folder) 
        os.makedirs('Imagenes', exist_ok = True)
        data = requests.get(folder)
        lista = []
        soup = BeautifulSoup(data.text, 'html.parser')
        p = soup.find_all('a', href = True)
        for pdfs in p:
            links = pdfs.get('href')
            if 'pdf' in links:
                lista.append(links)
        for n in range(len(lista)):
            file = open(f'pdfs{n+1}.pdf', 'wb')
            get = requests.get(lista[n])            
            for chunk in get.iter_content(100000):
                file.write(chunk)
        break