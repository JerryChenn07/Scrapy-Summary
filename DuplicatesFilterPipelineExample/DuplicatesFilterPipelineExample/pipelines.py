# -*- coding: utf-8 -*-
import pymongo
from scrapy.exceptions import DropItem


class DuplicatesFilterPipelineExamplePipeline(object):
    def process_item(self, item, spider):
        page = item['page']
        if page == '0':
            raise DropItem()
        else:
            return item


class MongoPipeline(object):
    def __init__(self, host, port, db, collection):
        self.host = host
        self.port = port
        self.db = db
        self.collection = collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MONGODB_HOST'),
            port=crawler.settings.get('MONGODB_PORT'),
            db=crawler.settings.get('MONGODB_DB'),
            collection=crawler.settings.get('MONGODB_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.mydb = self.client[self.db]
        self.mycollection = self.mydb[self.collection]

    def process_item(self, item, spider):
        print(item)
        self.mycollection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
