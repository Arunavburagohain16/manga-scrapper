import requests
import os
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

#MANGA_EXTRACTOR
count = 1
i = 0
flag = 0
while(True):
    #url = "https://readms.net/r/my_hero_academia/246/6252/"+str(count)
    url = "https://kissmanga.com/Manga/Kuro-no-Maou/Ch-002"#+str(count)
    #url = "https://kissmanga.com/Search/Manga/"
    #search_manga = input("Enter manga : ")
    #url = url + search_manga
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get(url)
    if(flag == 0):
        time.sleep(10)
    flag = 1
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")
    #print(soup)
    images1 = soup.findAll('img',{'src':re.compile('.jpg')})
    #if(images == []):
    images2 = soup.findAll('img',{'src':re.compile('.png')})
    images = images1 + images2
    image_list=[]
    for image in images:
        image_list.append(image['src'])
    for i in range(len(image_list)):
        image_url = image_list[i]
    #image_url = "http:"+image_url
    #driver.quit()
    #print(image_url)
        r = requests.get(image_url)
        with open("try"+str(count)+".png",'wb') as f:
            f.write(r.content)
        count += 1
