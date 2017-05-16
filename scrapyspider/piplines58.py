# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
# from scrapyspider.model import Zufang, Basemodel
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import *
#
# engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/alchemy', echo=True)
# Basemodel.metadata.create_all(engine)

class ScrapyspiderPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):

        # dbsession = sessionmaker(bind=engine)
        # session = dbsession()


        if item:

            price = int(item['price'])

            if (item['types']=='合租' and price <=1100 and price >=800 and '2室' in item['space']) \
                    or (item['types']=='单间' and  price <=1100 and price >=800 and '2室' in item['space']) \
                    or (item['types']=='整租' and price>=1200 and  price <=1500  and '1室' in item['space']) \
                    or  (item['types']=='整租' and price>=1200 and price <=2500  and '2室' in item['space']):

                print(item['space'])
                with open('out.txt','a',encoding='utf-8') as outfile:
                    json.dump(dict(item),outfile, ensure_ascii=False,indent=2)
                    outfile.write('\r\n')
                    # new_house = Zufang(name=item['name'],area=item['area'],price=price,types=item['type'],link=item['link'])
                    #
                    # session.add(new_house)
                    # session.commit()
                    # session.close()

