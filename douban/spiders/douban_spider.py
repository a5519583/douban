# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'douban_spider'
    # 允许的域名列表
    allowed_domains = ['movie.douban.com']
    # 入口url
    start_urls = ['https://movie.douban.com/top250']

    # 默认的解析方法
    def parse(self, response):
        # 循环电影的条目
        movie_list = response.xpath('//ol/li')
        for i in movie_list:
            # item文件导入
            douban_item = DoubanItem()
            # 详细进行数据解析
            douban_item['serial_number'] = i.xpath('.//em/text()').extract_first()
            douban_item['movie_name'] = i.xpath('.//a/span[1]/text()').extract_first()
            douban_item['evaluate'] = i.xpath('.//div[@class="star"]/span[4]/text()').extract_first().replace('人评价','')
            douban_item['star'] = i.xpath('.//div[@class="star"]/span[2]/text()').extract_first()
            douban_item['describe'] = (i.xpath('.//p[@class=""]/text()').extract_first()).strip()
            douban_item['introduce'] = i.xpath('.//p[@class="quote"]/span/text()').extract_first()
            # yield到pipelines里面去
            yield douban_item
        # 解析下一页
        next_link = response.xpath('//span[@class="next"]/link/@href').extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('https://movie.douban.com/top250'+next_link, callback=self.parse)
