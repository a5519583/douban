# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DoubanPipeline(object):
    def __init__(self):
        self.client = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = '770880',
            db = 'douban',
            charset = 'utf8'
        )
        self.cur = self.client.cursor()
    def process_item(self, item, spider):
        # sql = "insert into movie(serial_number, movie_name, introduce, star, evaluate, descb) values (item['serial_number'], item['movie_name'], item['introduce'], item['star'], item['evaluate'], item['describe']);"
        # sql = "insert into movie(serial_number, movie_name, introduce, star, evaluate, descb) values ('1', '2', '3', '4', '5', '6');"
        lis = (item['serial_number'], item['movie_name'], item['introduce'], item['star'], item['evaluate'], item['describe'])

        sql = "insert into movie (serial_number, movie_name, introduce, star, evaluate, descb) values (%s ,%s ,%s ,%s ,%s ,%s)"
        self.cur.execute(sql, lis )
        self.client.commit()
        return item

