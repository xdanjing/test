#!/usr/bin/env python
# --*-- encoding: utf-8 --*--

"""
@version: v1.0
@author: lu
@software: PyCharm
@file: itemsss.py
@time: 16-12-24 下午3:39
"""

import scrapy

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updatad = scrapy.Field(serializer = str)


class DiscountedProduct(Product):
    discount_percent = scrapy.Field(serializer=str)
    discount_expiration_date = scrapy.Field()


class SpecificProduct(Product):
    name = scrapy.Field(Product.fields['name'], serializer=int)

product = Product(name = 'Pyhton lxml', price = 1000)
product['stock'] = 'fadsfsa'

product2 = product.copy()
print product2
print dict(product2)
product3 = DiscountedProduct({'name': 'lxml study', 'price': 987, 'discount_percent': 123})
print product3
product5 = SpecificProduct({'price':'123fs'})
product4 = SpecificProduct(stock='fdasfs', name='rewxwasa')
print product4, product5
