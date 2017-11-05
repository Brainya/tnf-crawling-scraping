# -*- coding: utf-8 -*-
import json

from scrapy import Spider
from scrapy.http import Request
from thenorthfacedotcom.items import ThenorthfacedotcomItem

class ThenorthfaceSpider(Spider):
    name = "thenorthface"
    allowed_domains = ["www.thenorthface.com"]
    start_urls = [
        'https://www.thenorthface.com/shop/mens-jackets-vests', # mens
        'https://www.thenorthface.com/shop/mens-shirts-tops',
        'https://www.thenorthface.com/shop/mens-pants-shorts',
        'https://www.thenorthface.com/shop/shoes-mens',
        'https://www.thenorthface.com/shop/mens-accessories',
        'https://www.thenorthface.com/shop/womens-jackets-vests', # womens
        'https://www.thenorthface.com/shop/womens-shirts-tops',
        'https://www.thenorthface.com/shop/womens-pants-shorts',
        'https://www.thenorthface.com/shop/shoes-womens',
        'https://www.thenorthface.com/shop/womens-accessories',
        'https://www.thenorthface.com/shop/kids-boys', # kids
        'https://www.thenorthface.com/shop/kids-girls',
        'https://www.thenorthface.com/shop/kids-toddlers-2t-5',
        'https://www.thenorthface.com/shop/kids-infants-0m-24m'
        ]

    def parse(self, response):
        res = response.xpath("//*[@id='catalog-results']/section/header/a/@href").extract()
        for sel in res:
            if sel:
                yield Request(sel, self.parse_category)

    def parse_category(self, response):
        res = response.xpath("//*[@id='catalog-results']/section/header/a/@href").extract()
        for sel in res:
            if sel:
                yield Request(sel, self.parse_product)

    def parse_product(self, response):
        res = response.xpath("//*[@id='catalog-results']/div/div[2]/div[4]/a/@href").extract()
        for sel in res:
            if sel:
                yield Request(sel, self.parse_product_detail)

    def parse_product_detail(self, response):
        item = ThenorthfacedotcomItem()
        # item['category'] = ''
        # item['name'] = response.xpath("//*[@id='product-info']/h1").extract_first()
        # item['price'] = response.xpath("//*[@id='product-info']/div[1]/span[1]").extract_first()
        # item['image'] = ''
        # item['url'] = response.url()
        # item['size'] = response.xpath("div[{i}]/div[1]/figure/a").extract()
        item['description'] = response.xpath("//*[@id='container-4']/div[1]/section/div[1]/div/div").extract_first()
        yield item
