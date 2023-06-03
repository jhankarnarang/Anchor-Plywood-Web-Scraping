from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://finolex.com/wires-cables/')
soup = BeautifulSoup(source.content, 'lxml')

for main in soup.find_all('div',class_='col-sm-12'):
    img = main.find('div',class_='abt_img')
    try:
        prod_img = img.div.img['src']
        print(prod_img)
    except:
        print('')

    desc = main.find('div',class_='abt_txt')
    try:
        prod_desc = desc.p
        print(prod_desc)
    except:
        print('')

    

# for links in main.find_all('div',class_='col-sm-12'):
#     img = main.div.img
#     print(img)
