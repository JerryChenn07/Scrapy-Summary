# -*- coding: utf-8 -*-
import scrapy


class DuplicatesFilterPipelineExampleItem(scrapy.Item):
    # define the fields for your item here like:
    t1 = scrapy.Field()
    t2 = scrapy.Field()
    page = scrapy.Field()
