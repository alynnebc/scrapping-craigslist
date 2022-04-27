# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CraigslistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    compensation = scrapy.Field()
    employment_type = scrapy.Field()
    lat = scrapy.Field()
    long = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

class CraigslistNoImageItem(scrapy.Item):
    date = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()
    compensation = scrapy.Field()
    employment_type = scrapy.Field()
    lat = scrapy.Field()
    long = scrapy.Field()
    description = scrapy.Field()