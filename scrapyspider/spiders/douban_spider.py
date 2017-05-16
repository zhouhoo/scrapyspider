from scrapy.selector import Selector
from scrapyspider.items import DoubanZufangItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import  Request
from scrapy import log
import re

def NextURL():
    list_urls = ['https://www.douban.com/group/zf365/group/zf365/discussion?start='+i for i in range(0,25,250)]

    for next_url in list_urls:
        yield next_url

class FangSpider(CrawlSpider):
    name = "doubanspider"
    allowed_domains = ["www.douban.com"]
    start_urls = (
        #"https://www.douban.com/group/zf365/",
    )
    # rules = [         # 利用rule继续爬取下一页
    #     Rule(LinkExtractor(allow=["/group/zf365/discussion?start=\d+$"]), follow=True, callback='parse_item'),
    # ]

    url = NextURL()

    def start_requests(self):
        """
        NOTE: This method is ONLY CALLED ONCE by Scrapy (to kick things off).
        Get the first url to crawl and return a Request object
        This will be parsed to self.parse which will continue
        the process of parsing all the other generated URLs
        """

        ## grab the first URL to being crawling
        list_urls = ['https://www.douban.com/group/zf365/discussion?start='+ str(i) for i in range(0,300,25)]

        for url in list_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = Selector(response)

        sites = sel.xpath('//table[@class="olt"]/tr[@class=""]')
        items = []
        for site in sites:
            item = DoubanZufangItem()
            #print(site)
            title=site.xpath('td[@class="title"]/a')
            if title:
                item['title'] = title.xpath('text()').extract()[0]

                item['house_link'] = title.xpath('@href').extract()[0]


            name = site.xpath('td[@nowrap="nowrap"][1]/a')
            if name:
                item['name'] =name.xpath('text()').extract()[0]
                item['writer_page'] =name.xpath('@href').extract()[0]



            reply = site.xpath('td[@nowrap="nowrap"][2]/text()').extract()
            if reply:
                item['score_num'] = reply[0]

            datainfo = site.xpath('td[@nowrap="nowrap"][3]/text()').extract()
            if datainfo:
                item['reply_date']=datainfo[0]

            items.append(item)

        return items


if __name__ == "__main__":

    ss = '21世纪现代城，21世纪国际公寓，东渡国际青年城，文化名园，太平花苑，高尔夫国际花园，百家湖西花园，湖滨世纪花园，仲景公寓，百家湖利源国际公馆，海花苑，颐和美地'
    xiaoqu = ss.split('，')
    print(xiaoqu)



