# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入MongoDB
from pymongo import MongoClient

# 实例化MongoDB客户端
client =MongoClient()
# 实例化库(database)和表(Collection)
collection = client["tencent"]["tenxu_spider"]

class TencentPipeline(object):
    def process_item(self, item, spider):
    	print(item)
    	# 添加到数据到MongoDB里
    	collection.insert(item)
    	return item