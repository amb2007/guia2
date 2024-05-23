import pyperclip, requests
from bs4 import BeautifulSoup

paste = pyperclip.paste()

while True:
    folder = pyperclip.paste()
    if folder != paste :
        print(folder)
        break
data = requests.get(folder)
data.raise_for_status()
if data.status_code != 200:
    print('la pagina no es utilizable')
else:
    soup = BeautifulSoup(data.text, 'html.parser')
file = open('ej1', 'wb')
for chunk in data.iter_content(1000):
     file.write(chunk[:100])