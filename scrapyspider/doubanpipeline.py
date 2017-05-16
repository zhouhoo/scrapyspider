# -*- coding: utf-8 -*-

# Define your item pipelines here
import json


class ScrapyspiderPipeline(object):

    keywords = ['3号线','三号线','九龙湖','江宁','21世纪现代城', '21世纪国际公寓', '东渡国际青年城', '文化名园', '太平花苑',
              '高尔夫国际花园', '百家湖西花园', '湖滨世纪花园', '仲景公寓',
              '百家湖利源国际公馆', '海花苑', '颐和美地']

    def process_item(self, item, spider):

        # dbsession = sessionmaker(bind=engine)
        # session = dbsession()


        if item:
            title = item['title'].strip()
            if item['score_num']:
                reply = int(item['score_num'])
            else:
                reply =0

            if any(keyword in title for keyword in self.keywords) \
                    and (item['reply_date'].startswith('05')
                     or item['reply_date'].startswith('04-30'))\
                    and reply >=1 :

                    print(item)
                    with open('out.txt','a',encoding='utf-8') as outfile:
                        json.dump(dict(item),outfile, ensure_ascii=False,indent=2)
                        outfile.write('\r\n')
                    # new_house = Zufang(name=item['name'],area=item['area'],price=price,types=item['type'],link=item['link'])
                    #
                    # session.add(new_house)
                    # session.commit()
                    # session.close()

