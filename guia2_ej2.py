import pyperclip, requests, webbrowser
from bs4 import BeautifulSoup

paste = pyperclip.paste()

while True:
    folder = pyperclip.paste()
    if paste != folder :
        print(folder)
        print('hola')
        print(paste)
        break
print('hola')
data = requests.get(folder)
data.raise_for_status()
if data.status_code != 200:
    print('la pagina no es utilizable')
else:
    soup = BeautifulSoup(data.text, 'html.parser')
    lista = list(soup.find_all('p'))
    for i in lista:
        print(i.text)