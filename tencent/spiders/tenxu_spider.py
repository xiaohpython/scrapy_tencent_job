# -*- coding: utf-8 -*-
import scrapy


class TenxuSpiderSpider(scrapy.Spider):
    name = 'tenxu_spider'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath("//table[@class='tablelist']/tr")[:-1]
        for tr in tr_list:
        	item ={}
        	item["title"] =tr.xpath("./td[1]/a/text()").extract_first()
        	item["position"] =tr.xpath("./td[2]/text()").extract_first()
        	item["add"] =tr.xpath("./td[4]/text()").extract_first()
        	item["date"] =tr.xpath("./td[5]/text()").extract_first()
        	yield item

        #获取下一页
        next_url =response.xpath("//a[@id='next']/@href").extract_first()
        if next_url != "javascrapt;;":
        	next_url ="http://hr.tencent.com/" +next_url
        	yield scrapy.Request(
        		next_url,
        		callback=self.parse
        		)
