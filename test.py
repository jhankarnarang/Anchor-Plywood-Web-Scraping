from bs4 import BeautifulSoup
import requests
import csv

t=[]
def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Prod_links','Prod_name','Image Links','Prod_Code','Product Description','Prod_feature'])

            print(f'> {sections[i]}')
            source = requests.get(sections[i])
            soup = BeautifulSoup(source.content, 'lxml')

            for airlink in soup.find_all('div',class_='product-img-box mb-4'):
                airlinks = airlink.a['href']
                if 'https://www.lifelongindiaonline.com/' not in airlinks:
                    airlinkss = f'https://www.lifelongindiaonline.com/{airlinks}'
                    
                    print(airlinkss)


                    source = requests.get(airlinkss)
                    soup = BeautifulSoup(source.content, 'lxml')

                    
                    for img in soup.find_all('li',class_='image-item'):
                        image = img.img['src']
                        if 'https:' not in image:
                            prod_img = f'https:{image}'
                        print(prod_img)
                    name = soup.find('h5',class_='ll-color hind-medium')
                    prod_name = name.text
                    print(prod_name)
                    code = soup.find('h6',class_='sku hind-light').text
                    print(code.replace('\n',''))
                    description = soup.find('span',class_='light-grey-color primary-size d-block w-xl-80').text
                    desc = description.replace(u'\xa0', u'')
                    desc = desc.replace('\n','')
                    print(desc)
                    t.append(airlinkss)
                    t.append(prod_name)
                    t.append(prod_img)
                    t.append(code)
                    t.append(desc)
                    
                    
                    try:
                        feature = soup.find('p',class_='ll-text font-weight-light primary-size').text
                        feature=feature.replace('\n','')
                        feature=feature.strip()
                        
                        t.append(feature)
                        print(feature)
                        print(t)
                        csv_writer.writerow([airlinkss, prod_name,prod_img,code,desc,feature])
                    except:
                        print('')
                        csv_writer.writerow([airlinkss, prod_name,prod_img,code,desc])


            

            
            


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

    sections = ['https://www.lifelongindiaonline.com//collections/kitchen/llck-air-fryer/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-bread-maker/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-cookware/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-egg-boiler/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-gas-stoves/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-hand-blender/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-hand-mixer/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-ice-cream-maker/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-inductions/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-kettles/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-mixer-grinders/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-oven-toaster-griller/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-pressure-cookers/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-sandwich-makers/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-stand-mixer/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-waffle-maker/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/kitchen/llck-wet-grinder/#skip-tags-row',
                'https://www.lifelongindiaonline.com//collections/home/llck-air-cooler/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-ceiling-fans/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-dry-iron/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-exhaust-fans/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-pedestral-fan/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-refrigerators/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-room-heater/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-table-fan/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-tower-fan/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-vacuum-cleaner/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-voltage-stabilizers/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-wall-fan/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-washing-machines/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/home/llck-water-heater/#skip-tags-row',
                'https://www.lifelongindiaonline.com//collections/fitness/llck-exercise-bikes/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/fitness/llck-cycle/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/fitness/llck-gun-massager/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/fitness/llck-home-gym/#skip-tags-row','https://www.lifelongindiaonline.com/collections/fitness/llck-home-gym?page=2','https://www.lifelongindiaonline.com/collections/fitness/llck-home-gym?page=3', 'https://www.lifelongindiaonline.com//collections/fitness/llck-specials/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/fitness/llck-treadmills/#skip-tags-row','https://www.lifelongindiaonline.com/collections/fitness/llck-treadmills?page=2', 'https://www.lifelongindiaonline.com//collections/fitness/llck-weighing-scale/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/fitness/llck-yoga-mats/#skip-tags-row',
                'https://www.lifelongindiaonline.com//collections/grooming/llck-eyebrow-trimmer/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/grooming/llck-face-spatula/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/grooming/llck-female-grooming/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/grooming/llck-hair-curler/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/grooming/llck-male-grooming/#skip-tags-row',
                'https://www.lifelongindiaonline.com//collections/lifestyle/llck-air-pressure-massager/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-body-massagers/#skip-tags-row','https://www.lifelongindiaonline.com/collections/lifestyle/llck-body-massagers?page=2', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-cushion-massager/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-dental-care/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-face-massagers/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-facial-steamer/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-female-grooming/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-foot-leg/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-foot-leg-massagers/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-gun-massager/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-humidifier/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-pain-relief/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/lifestyle/llck-tens-massager/#skip-tags-row',
                'https://www.lifelongindiaonline.com//collections/smart-home/llck-ir-blaster/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/smart-home/llck-sensors/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/smart-home/llck-smart-bulbs/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/smart-home/llck-smart-plug/#skip-tags-row', 'https://www.lifelongindiaonline.com//collections/smart-home/llck-video-doorbell/#skip-tags-row',
                'https://www.lifelongindiaonline.com//collections/accessories/llck-power-bank/#skip-tags-row'   
    ]  

    file_names = [
        './data/kitchen/air-fryer.csv',
        './data/kitchen/Bread-maker.csv',
        './data/kitchen/cook-ware.csv',
        './data/kitchen/egg-boiler.csv',
        './data/kitchen/gas-stoves.csv',
        './data/kitchen/hand-blender.csv',
        './data/kitchen/hand-mixer.csv',
        './data/kitchen/Ice-cream-maker.csv',
        './data/kitchen/induction.csv',
        './data/kitchen/kettles.csv',
        './data/kitchen/mixer-grinder.csv',
        './data/kitchen/oven-toater.csv',
        './data/kitchen/pressure-cooker.csv',
        './data/kitchen/sandwich-makeer.csv',
        './data/kitchen/stand-mixer.csv',
        './data/kitchen/waffle-maker.csv',
        './data/kitchen/wet-grinder.csv',
        './data/home/air-cooler.csv',
        './data/home/ceiling-fans.csv',
        './data/home/dry-iron.csv',
        './data/home/exhaust-fans.csv',
        './data/home/Pedestral-fans.csv',
        './data/home/refrigretor.csv',
        './data/home/room-heaters.csv',
        './data/home/table-fan.csv',
        './data/home/tower-fans.csv',
        './data/home/vacuum-cleaner.csv',
        './data/home/voltage-stabiliser.csv',
        './data/home/wall-fans.csv',
        './data/home/waashing-machines.csv',
        './data/home/water-heaters.csv',
        './data/fitness/excercise-bikes.csv',
        './data/fitness/cycle.csv',
        './data/fitness/gun-massager.csv',
        './data/fitness/home-gym-page1.csv',
        './data/fitness/home-gym-page2.csv',
        './data/fitness/home-gym-page3.csv',
        './data/fitness/specials.csv',
        './data/fitness/tread-mills-page1.csv',
        './data/fitness/tread-mills-page2.csv',
        './data/fitness/weighing-scale.csv',
        './data/fitness/yoga-mats.csv',
        './data/grooming/eyebrow-trimmer.csv',
        './data/grooming/face-spatula.csv',
        './data/grooming/female-grooming.csv',
        './data/grooming/hair-curler.csv',
        './data/grooming/male-grooming.csv',
        './data/lifestyle/air-pressure-massager.csv',
        './data/lifestyle/body-massager-page1.csv',
        './data/lifestyle/body-massager-page2.csv',
        './data/lifestyle/cushion-massager.csv',
        './data/lifestyle/dental-care.csv',
        './data/lifestyle/face-massager.csv',
        './data/lifestyle/facial-steamer.csv',
        './data/lifestyle/female-grooming.csv',
        './data/lifestyle/foot&leg.csv',
        './data/lifestyle/foot&leg-massagers.csv',
        './data/lifestyle/gun-massager.csv',
        './data/lifestyle/humidifier.csv',
        './data/lifestyle/pain-relief.csv',
        './data/lifestyle/tens-massager.csv',
        './data/smarthome/IR-Blaster.csv',
        './data/smarthome/Sensors.csv',
        './data/smarthome/Smart-bulbs.csv',
        './data/smarthome/smart-plugs.csv',
        './data/smarthome/Video-doorbell.csv',
        './data/accessories/Powerbank.csv',
        ]

    scrape(sections, file_names)