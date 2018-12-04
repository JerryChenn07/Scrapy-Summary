# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DuplicatesFilterPipelineExampleItem(scrapy.Item):
    # define the fields for your item here like:
    t1 = scrapy.Field()
    t2 = scrapy.Field()
    page = scrapy.Field()
