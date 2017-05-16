# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanZufangItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 发布者
    name = scrapy.Field()
    # 时间
    reply_date = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()
    #租房详情
    house_link = scrapy.Field()

    #作者主页
    writer_page = scrapy.Field()

class ZufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 标题
    area = scrapy.Field()  # 商圈
    price = scrapy.Field() # 价位
    space = scrapy.Field() # 户型
    types = scrapy.Field() #　租赁类别
    link = scrapy.Field() #　详情链接
    #people = scrapy.Field() # 经纪人


class Zufang365Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 标题
    area = scrapy.Field()  # 商圈
    price = scrapy.Field() # 价位
    space = scrapy.Field() # 户型
    types = scrapy.Field() #　租赁类别
    direction = scrapy.Field() # 朝向
    floors = scrapy.Field() # 楼层
    link = scrapy.Field() #　详情链接
    people = scrapy.Field() # 经纪人