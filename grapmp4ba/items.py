# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Mp4BaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    definition = scrapy.Field()
    pic_path = scrapy.Field()
    dl_link = scrapy.Field()
    detail = scrapy.Field()
    hashcode= scrapy.Field() 
