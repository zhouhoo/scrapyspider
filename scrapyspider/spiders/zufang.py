from scrapy.selector import Selector
from scrapyspider.items import Zufang365Item
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re

class FangSpider(CrawlSpider):
    name = "fang365"
    allowed_domains = ["nj.rent.house365.com"]
    start_urls = (
        'http://nj.rent.house365.com/district_d8/dl_x1-j99-kp800-kq2500.html',
    )
    rules = [         # 利用rule继续爬取下一页
        Rule(LinkExtractor(allow=("/district_d8/dl_x1-j99-kp800-kq2500-p\d+", )), follow=True, callback='parse_item'),
    ]

    def parse_item(self, response):
        sel = Selector(response)
        pattern = re.compile(r'\d+')
        sites = sel.xpath('//dl[@id="JS_listPag"]/dd')
        items = []
        for site in sites:
            item = Zufang365Item()
            #print(site)
            title=site.xpath('div[@class="info"]/h3/a')
            if title:
                item['name'] = title.xpath('text()').extract()[0]

                item['link'] = title.xpath('@href').extract()[0]


            price = site.xpath('div[@class="price"]/span/text()').extract()
            if price:
                item['price'] =price[0]

            area = site.xpath('div[@class="info"]/div[@class="item"][1]/a/text()').extract()
            if area:
                item['area'] = area[0].strip()

            houseinfo = site.xpath('div[@class="info"]/div[@class="item"][2]/text()').extract()
            #print(houseinfo)
            if houseinfo:
                item['types'] =houseinfo[0].strip()
                item['space'] =houseinfo[2].strip()
                if len(houseinfo) >=6:
                    item['direction']=houseinfo[3].strip()
                    item['floors'] = pattern.findall(houseinfo[5])[0]
                else:
                    item['floors'] = pattern.findall(houseinfo[4])[0]

            peopleinfo = site.xpath('div[@class="info"]/div[@class="item"][3]/text()').extract()
            if peopleinfo:
                item['people'] = peopleinfo[0]

            items.append(item)
        return items


if __name__ == "__main__":

    keywords = ['3号线','三号线','九龙湖','江宁','21世纪现代城', '21世纪国际公寓', '东渡国际青年城', '文化名园', '太平花苑',
                '高尔夫国际花园', '百家湖西花园', '湖滨世纪花园', '仲景公寓',
                '百家湖利源国际公馆', '海花苑', '颐和美地']

    if any(keyword in "三号线九龙湖单间出租（6月可入住）" for keyword in keywords):
        print(1)



