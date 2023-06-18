from bs4 import BeautifulSoup
import requests
import csv


def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Prod_links','Prod_name','Image Links','Prod_About','Product_Key_Features','Prod_warranty'])

            print(f'> {sections[i]}')
            source = requests.get(sections[i])
            soup = BeautifulSoup(source.content, 'lxml')
            for link in soup.find_all('div',class_='productGrid-productImg'):
                links = link.a['href']
                if 'https://www.racold.com/electric-instant-heater/pronto-stylo' not in links:
                    prod_link = f'https://www.racold.com{links}'
                    print(prod_link)

                    prod_source = requests.get(prod_link)
                    prod_soup = BeautifulSoup(prod_source.content, 'lxml')
                    prod_name = prod_soup.find('h1',class_='product-title').span.text
                    print(prod_name)
                    img = prod_soup.find('div',class_='carousel-inner').img['src']
                    if 'https://www.racold.com/electric-instant-heater/pronto-stylo' not in img:
                        prod_img = f'https://www.racold.com{img}'
                        print(prod_img)
                    desc = prod_soup.find('div',class_='classic-tabs mx-2 mt-4')

                    for info in desc.find_all('div',class_='tab-content card'):
                        try:
                            prod_about =info.p.text
                        except:
                            print('')
                        try :
                            prod_info = info.ul.text
                            prod_warr1 = info.find_next('div',class_='tab-pane fade',id='WARRANTY').text
                            
                            
                        except:
                            print('')
                            


                        try :
                            prod_info = info.ul.text
                            prod_warr = info.find_next('div',class_='tab-pane fade',id='warranty').text
                            
                            
                        except:
                            print('')
                            
                        csv_writer.writerow([prod_name,prod_img,prod_about,prod_info,prod_warr,prod_warr1])


            

            
            


if __name__ == '__main__':

    '''
    usage:
    -> install requirements
    -> verify:
        - all site sections are listed in `sections`
        - all sites have a corresponding csv file `file_names`
        - all paths to the csv file are correct
    -> run
    '''

    sections = ['https://www.racold.com/electric-instant-heater',
                'https://www.racold.com/electric-storage-geyser',
                'https://www.racold.com/online-instantaneous-geyser',
                'https://www.racold.com/gas-water-heaters',
                'https://www.racold.com/solar-water-heaters',
                'https://www.racold.com/heat-pump-water-heaters'
    ]  

    file_names = [
        './data/electric-instant-geyser.csv',
        './data/electric-storage-geyser.csv',
        './data/online-instanataneous.csv',
        './data/gas-geyser.csv',
        './data/solar-geyser.csv',
        './data/heat-pump-geyser.csv'
        ]

    scrape(sections, file_names)