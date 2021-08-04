from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://kissmanga.com',allow_redirects=True)
bs = BeautifulSoup(html, 'html.parser')
print(bs)
#images = bs.find_all('img', {'src':re.compile('.jpg')})
#for image in images:
#    print(image['src']+'\n')
