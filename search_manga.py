import requests
import os
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

#MANGA_EXTRACTOR
cou = 0
count = 0
i = 0
flag = 0
search_manga = input("Enter manga : ")
os.mkdir(search_manga)
while(True):
    #===========================================================================
    url = "https://kissmanga.com/Search/Manga/"
    url = url + search_manga
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get(url)
    if(flag == 0):
        time.sleep(10)
    flag = 1
    #===========================================================================
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")
    link_list = []
    for link in soup.findAll('a', href  = True):
        link_list.append(link.get('href'))
    #===========================================================================
    lo = []
    c = 0
    for i in range(len(link_list)):
        if(link_list[i] != '#'):
            temp = link_list[i].split('/')
            if(temp[1] == 'Manga'):
                lo.append(link_list[i])
                print(c,lo[c])
                c += 1
            else:
                pass
    l1 = link_list[12].split('/')
    #===========================================================================
    #l1 = lo[manga_select].split('/')
    #l2 = link_list[32].split('/')
    print(l1)
    #print(l2)
    #===========================================================================
    if(l1[1] == 'Manga'):
        manga_select = int(input("Enter the manga list number : "))
        print('Searching...')
        driver.get('https://kissmanga.com'+lo[manga_select])
        #=======================================================================
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html.parser")
        l = []
        for link in soup.findAll('a', href  = True):
            l.append(link.get('href'))
        print('Searching.........')
        chapter = []
        c = 0
        for i in range(len(l)):
            #print(i,l[i])
            if(l[i] != '#'):
                temp = l[i].split('/')
                if(temp[1] == 'Manga'):
                    chapter.append(l[i])
                    print(c,chapter[c])
                    c += 1
                else:
                    pass
            #===================================================================
        count = 0
        while(True):
            num = -1-count
            driver.get('https://kissmanga.com'+chapter[num])
            count += 1
            if(count == len(chapter)):
                break
            else:
                content = driver.page_source.encode('utf-8').strip()
                soup = BeautifulSoup(content, "html.parser")
                #print(soup)
                images1 = soup.findAll('img',{'src':re.compile('.jpg')})
                images2 = soup.findAll('img',{'src':re.compile('.png')})
                images = images1 + images2
                image_list=[]
                for image in images:
                    try:
                        #image_list.append(image['src'])
                        print(image)
                        print(" (^_^)     Downloading....       (^_^) " )
                        r = requests.get(image['src'])
                        dir = os.path.join(search_manga,search_manga+str(cou)+".png")
                        with open(dir,'wb') as f:
                            f.write(r.content)
                        cou += 1
                    except:
                        pass
                print("          Done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #=======================================================================
    else:
        try:
            #=======================================================================
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content, "html.parser")
            l = []
            for link in soup.findAll('a', href  = True):
                l.append(link.get('href'))
            print("Searching.........")
            chapter = []
            c = 0
            for i in range(len(l)):
                #print(i,l[i])
                if(l[i] != '#'):
                    temp = l[i].split('/')
                    if(temp[1] == 'Manga'):
                        chapter.append(l[i])
                        print(c,chapter[c])
                        c += 1
                    else:
                        pass
                #===================================================================
            count = 0
            while(True):
                num = -1-count
                driver.get('https://kissmanga.com'+chapter[num])
                count += 1
                if(count == len(chapter)):
                    break
                else:
                    content = driver.page_source.encode('utf-8').strip()
                    soup = BeautifulSoup(content, "html.parser")
                    #print(soup)
                    images1 = soup.findAll('img',{'src':re.compile('.jpg')})
                    images2 = soup.findAll('img',{'src':re.compile('.png')})
                    images = images1 + images2
                    image_list=[]
                    for image in images:
                        try:
                            #image_list.append(image['src'])
                            print(image)
                            print(" (^_^)     Downloading....       (^_^) " )
                            r = requests.get(image['src'])
                            dir = os.path.join(search_manga,search_manga+str(cou)+".png")
                            with open(dir,'wb') as f:
                                f.write(r.content)
                            cou += 1
                        except:
                            pass
                    print("Done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    #===========================================================================
        except:
            print("         (>_<)    Manga not found!!!!!!!!!   (>_<)          ")
    #driver.quit()
    break
