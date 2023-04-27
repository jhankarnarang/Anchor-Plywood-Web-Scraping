from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://anchorplywood.com/ProductNew.aspx?CategoryId=1023')
soup = BeautifulSoup(source.content, 'lxml')

for links in soup.find_all('div',class_='col-md-4 col-xs-4 col-sm-6 cs-full-wd480'):
    p_link = links.a['href']
    prod_link = f'https://anchorplywood.com/{p_link}'
    print(f"'{prod_link}',")