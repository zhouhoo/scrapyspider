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

    xiaoqu = ['21世纪现代城', '21世纪国际公寓', '东渡国际青年城', '文化名园', '太平花苑',
              '高尔夫国际花园', '百家湖西花园', '湖滨世纪花园', '仲景公寓',
              '百家湖利源国际公馆', '海花苑', '颐和美地']
    # def __init__(self):
    #     with open("result.html",'a',encoding='utf-8') as file:
    #         file.writelines('<html><head>')
    #         file.writelines('<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>')
    #         file.writelines('<title>Rent Crawer Result</title></head><body>')
    #         file.writelines('<table rules=all>')
    #         file.writelines('<h1>筛选后的租房信息展示</h1>')
    #         file.writelines(
    #             '<tr><td>标题</td><td>详情链接</td><td>位置</td><td>租金</td><td>户型</td><td>租房方式</td><td>楼层</td><td>房东</td></tr>')
    #
    # def __del__(self):
    #     with open("result.html",'a',encoding='utf-8') as file:
    #         file.writelines('</table>')
    #         file.writelines('</body></html>')


    def process_item(self, item, spider):

        # dbsession = sessionmaker(bind=engine)
        # session = dbsession()


        if item:
            floors = int(item['floors'])

            price = int(item['price'])
            if item['area'] in self.xiaoqu and item['types']=='合租' \
                    and price <=1100 and price >=800 and floors>=3 and \
                    ('2室' in item['space'] or '3室' in item['space']):



                with open('result.txt','a',encoding='utf-8') as outfile:


                    json.dump(dict(item),outfile, ensure_ascii=False,indent=2)
                    outfile.write('\r\n')

                # new_house = Zufang(name=item['name'],area=item['area'],price=price,types=item['type'],link=item['link'])
                #
                # session.add(new_house)
                # session.commit()
                # session.close()

