# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

class EmailspiderSpider(scrapy.Spider):
    name = 'emailspider'
    allowed_domains = ['']
    start_urls = ['https://www.asx.com.au/contact/#/']

    def start_requests(self):
        #query = input("Enter your query: ")
        for url in self.start_urls:
            #yield scrapy.Request("{}{}".format(url, query))
            yield scrapy.Request(url)

    def parse(self, response):
        url_to_follow = LxmlLinkExtractor(allow=()).extract_links(response)
        url_to_follow = [str(link.url) for link in url_to_follow]
        url_to_follow.append(str(response.url))
        for url in url_to_follow:
            yield scrapy.Request(
                url=url, callback=self.parse_email, dont_filter=True)

    def parse_email(self, response):
        html_str = response.text
        emails = self.extract_email(html_str)
        phone_no = self.extract_phone_number(html_str)
        yield{
            "url": response.url,
            "emails": emails,
            "phone numbers": phone_no
        }

    def extract_email(self, html_as_str):
        return re.findall(r'[\w\.-]+@[\w\.-]+', html_as_str)

    def extract_phone_number(self, html_as_str):
        return re.findall(r'\+\d{2}\s?0?\d{10}', html_as_str)
