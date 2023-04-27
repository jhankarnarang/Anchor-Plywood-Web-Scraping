from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Links','name', 'img','Prod_desc','Prod_salient_features','Prd_properties','Prod_Technical_data'])

            print(f'> {sections[i]}')
            
            
            url = f'{sections[i]}'
            source = requests.get(url)
            soup = BeautifulSoup(source.content, 'lxml')

            img = soup.find("div",class_='col-md-5 col-sm-4 products')
            prod_img = img.li.img['src']
            prod_img = prod_img.replace(' ','%20')
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
            try:
                main2 = soup.find('div',class_='col-md-12 col-sm-12 pro-specification')
                salient_feature = main2.ul.text.replace('\r\n\t\t','').lstrip()
                salient_feature = salient_feature.replace('\n','')
                print(salient_feature)
                csv_writer.writerow([sections[i],prod_name,prod_img,prod_desc,salient_feature])
            except:
                print('')
                csv_writer.writerow([sections[i],prod_name,prod_img,prod_desc])
            try:
                dfs = pd.read_html(url)
                                                                                                                    
                df = dfs[0]
                df1 = dfs[1]
                pd.set_option('max_colwidth', 400)
                print(df)
                print(df1)
                df.to_csv('Anchor_executive_marine_tables.csv')
                df1.to_csv('Anchor_fire_retardant_marine_tables.csv')
            except:
                print('')
                
            



            

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
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1022',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1020',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1021',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1039',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=20',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1038',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1042',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1040',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1025',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1024',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1023',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1044',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1033',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1035',
        'https://anchorplywood.com/ProductDescription.aspx?ProductId=1030',
        ]

    file_names = [
        './data/marineplywoods/Anchor_executive.csv',
        './data/marineplywoods/Anchor_fire.csv',
        './data/marineplywoods/Anchor_72.csv',
        './data/marineplywoods/Anchor_marine.csv',
        './data/marineplywoods/Anchor_2000_marine.csv',
        './data/marineplywoods/Anchor_seavk_marine.csv',
        './data/commercialplywoods/gurjan_commercial.csv',
        './data/commercialplywoods/Anchor_commercial.csv',
        './data/commercialplywoods/Anchor_2000_commercial.csv',
        './data/commercialplywoods/Anchor_sevak_commercial.csv',
        './data/blockboards/Anchor_blockboard(Exterior Grade).csv',
        './data/blockboards/Blockboard(Interior Grade).csv',
        './data/flushdoors/Anchor_fire-retardant_flush_doors.csv',
        './data/flushdoors/Anchor_flush_doors.csv',
        './data/shutteringplywood/Anchor_densified_film_faced_shuttering-plywood.csv'
    ]

    scrape(sections, file_names)