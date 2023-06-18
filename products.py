from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('step-lights.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_name','prod_img','prod_about','prod_info','prod_warr'])

source = requests.get('https://www.racold.com/heat-pump-water-heaters/commercial')
soup = BeautifulSoup(source.content, 'lxml')

prod_name = soup.find('h1',class_='product-title').span.text
print(prod_name)
img = soup.find('div',class_='carousel-inner').img['src']
if 'https://www.racold.com/electric-instant-heater/pronto-stylo' not in img:
    prod_img = f'https://www.racold.com{img}'
    print(prod_img)
desc = soup.find('div',class_='classic-tabs mx-2 mt-4')

for info in desc.find_all('div',class_='tab-content card'):
    try:
        prod_about =info.p.text
    except:
        print('')
    try :
        prod_info = info.ul.text
        prod_warr = info.find_next('div',class_='tab-pane fade',id='WARRANTY').text
        csv_writer.writerow([prod_name,prod_img,prod_about,prod_info,prod_warr])
        
    except:
        print('')


    try :
        prod_info = info.ul.text
        prod_warr = info.find_next('div',class_='tab-pane fade',id='warranty').text
        csv_writer.writerow([prod_name,prod_img,prod_about,prod_info,prod_warr])
        
    except:
        print('')


print(prod_about)
print(prod_info)












