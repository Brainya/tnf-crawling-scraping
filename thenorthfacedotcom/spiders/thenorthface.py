# -*- coding: utf-8 -*-
import json
import re

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
                if re.match('https://www.thenorthface.com/shop/kids', sel): # jump to product if for kids
                    yield Request(sel, self.parse_product)
                else:
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
        item['name'] = response.xpath("//div[@id='product-info']/h1/text()").extract_first()
        item['category'] = response.xpath("//nav[@id='pdp-breadcrumb']/ul/li[last()]/a/text()").extract_first()
        price = response.xpath("//section[@id='container-4']/div[@itemtype='http://schema.org/Product']/span[last()]/meta[1]/@content").extract_first()
        item['price'] = '$' + price
        image = response.xpath("//form[@id='product-attr-form']/section[1]/div[2]/div/label[1]/img/@src").extract_first()
        item['image'] = 'https:' + re.sub(r'\?\$([a-zA-Z0-9]*)\$', '', image) # full size + add 'https:'
        item['description'] = response.xpath("//div[@class='desc-container pdp-details-desc-container']/text()").extract_first().strip()
        item['url'] = response.url
        yield item
