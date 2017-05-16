from scrapy.selector import Selector
from scrapyspider.items import ZufangItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class FangSpider(CrawlSpider):
    name = "58fang"
    allowed_domains = ["nj.58.com"]
    start_urls = (
        'http://nj.58.com/njkaifaqu/chuzu/',
    )
    rules = [         # 利用rule继续爬取下一页
        Rule(LinkExtractor(allow=("/chuzu/pn\d+/", )), follow=True, callback='parse_item'),
    ]
    def parse_item(self, response):
        sel = Selector(response)
        sites = sel.xpath('//li[@logr]')
        items = []
        for site in sites:
            item = ZufangItem()
            #print(site)
            title=site.xpath('div[@class="des"]/h2/a')
            if title:
                name = title.xpath('text()')
                temp = name[0].extract().strip().split(' ')
                item['name'] = name[0].extract().strip()

                item['types'] = temp[0]
                if len(temp)>=3:
                    item['area'] = temp[2]

                item['link'] = title.xpath('@href').extract()[0]

            price = site.xpath('div[@class="listliright"]/div[@class="money"]/b/text()')
            if price:
                item['price'] =price.extract()[0]

            space = site.xpath('div[@class="des"]/p[@class="room"]/text()')
            if space:

                item['space'] = space.extract()[0].strip()
            # people = site.xpath('span[@class="listjjr"]/a/text()')
            # if people:
            #     item['people'] = people.extract()

            items.append(item)
        return items




