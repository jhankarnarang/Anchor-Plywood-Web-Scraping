from bs4 import BeautifulSoup
import requests
import csv


def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['name', 'img','desc'])

            print(f'> {sections[i]}')
            section_source = requests.get(sections[i])
            soup = BeautifulSoup(section_source.content, 'lxml')
            try:
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

                csv_writer.writerow([prod_name,prod_img,product_desc])
            except:
                    print('')

            for main1 in soup.find_all('div',class_='col-sm-4'):
                try :
                        img1 = main1.img['src']
                        if 'pdf.png' not in img1:
                                print(img1)
                                csv_writer.writerow([img1])
                
                except:
                        print('')

                
                        
                info1 = main1.text
                
                desc1 = info1.replace('Download Brochure(PDF 2.2MB)','')
                prod_desc1 = (','.join(desc1.splitlines()))
                print(prod_desc1)
                csv_writer.writerow([prod_desc1])


            

            
            


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

    sections = [
        'https://finolex.com/wires-cables/',
        'https://finolex.com/switches/',
        'https://finolex.com/led-lightings/',
        'https://finolex.com/fan/',
        'https://finolex.com/finolex-mcb/',
        'https://finolex.com/water-heater/',
        'https://finolex.com/optical-fibre-cables/'
           ]

    file_names = [
        './data/wires-cables.csv',
        './data/switches.csv',
        './data/led-lightings.csv',
        './data/fan.csv',
        './data/finolex-mcb.csv',
        './data/water-heater.csv',
        './data/optical-fibre.csv'
    ]

    scrape(sections, file_names)