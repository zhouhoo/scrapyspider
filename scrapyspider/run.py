# -*- coding: utf-8 -*-



from scrapy import cmdline


#name = 'fang365'
#name='58fang'
name = 'doubanspider'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())