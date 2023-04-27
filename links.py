from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://anchorplywood.com/ProductNew.aspx?CategoryId=22')
soup = BeautifulSoup(source.content, 'lxml')

for links in soup.find_all('div',class_='col-md-4 col-xs-4 col-sm-6 cs-full-wd480'):
    p_link = links.a['href']
    prod_link = f'https://anchorplywood.com/{p_link}'
    print(f'>>{prod_link}')

    url = f"'{prod_link}'"
    source = requests.get(prod_link)
    soup = BeautifulSoup(source.content, 'lxml')
    img = soup.find("div",class_='col-md-5 col-sm-4 products')
    prod_img = img.li.img['src']
    print(prod_img)

    main = soup.find('div',class_='col-md-6 col-sm-6 pro-description')
    cat_name=main.h4.span.text
    print(cat_name)
    prod_name = main.h5.span.text
    print(prod_name)

    prod_desc = main.div.text
    prod_desc = prod_desc.replace('\n\n','')
    prod_desc= prod_desc.replace('\n\r\n','')
    prod_desc = prod_desc.replace('\t',' ')
    print(prod_desc)

    main2 = soup.find('div',class_='col-md-12 col-sm-12 pro-specification')
    salient_feature = main2.ul.text.replace('\r\n\t\t','').lstrip()
    print(salient_feature.replace('\n',''))
    
    print(url)
    dfs = pd.read_html(url)
                                                                                                        
    df = dfs[0]
    df1 = dfs[1]
    pd.set_option('max_colwidth', 120)
    print(df)
    print(df1)
    #csv_writer.writerow([df,df1])
    
