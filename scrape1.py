from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://finolex.com/wires-cables/')
soup = BeautifulSoup(source.content, 'lxml')

#for main in soup.find_all("div",class_='container'):

img = soup.find('div',class_='abt_img')
prod_img = img.div.img['src']
print(prod_img)

desc = soup.find('div',class_='abt_txt')
prod_name = desc.h4.text
print(prod_name)
prod_desc = desc.select('p')
listToStr = ' '.join([str(elem) for elem in prod_desc])
s = listToStr.replace('<p>','')
product_desc = s.replace('</p>','')
print(product_desc)


