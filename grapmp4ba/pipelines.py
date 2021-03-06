# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from grapmp4ba.model import Movie, DBSession
import time
import cgi
import re


class Grapmp4BaPipeline(object):

    def process_item(self, item, spider):
        detail = cgi.escape('<br>'.join(filter(lambda x: x!='', [x.strip().encode('utf-8', 'ignore') for x in item['detail']])))

        pattern = re.compile('(?<=HD|BD)\d+(?=P)')
        pattern2 = re.compile('(?<==)\w+')

        definition = pattern.search(item['title'].encode('utf-8', 'ignore')).group() if pattern.search(item['title'].encode('utf-8', 'ignore')) else None
        hashcode = pattern2.search(item['link']).group() if pattern2.search(item['link']) else None
        print item['title'].encode('utf-8', 'ignore')
        print item['link']
        print definition
        print hashcode
        print detail
        movie = Movie(title=item['title'].encode('utf-8', 'ignore'),
                      date_id=time.strftime('%Y%m%d'),
                      link=item['link'],
                      definition=definition,
                      pic_path=item['pic_path'],
                      dl_link=item['dl_link'],
                      detail=detail,
                      hashcode=hashcode
                      )
        if self.session.query(Movie(hashcode=hashcode)):
            print 'processed, skip.'
            exit(0)
        try:
            self.session.add(movie)
            self.session.commit()
        except Exception, e:
            print e
            raise e
        

    def open_spider(self, spider):
        self.session = DBSession()

    def close_spider(self, spider):
        self.session.close()
