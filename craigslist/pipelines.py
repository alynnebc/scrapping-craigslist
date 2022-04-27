# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from slugify import slugify
from craigslist.items import CraigslistItem

# class CraiglistPipeline:
#     def process_item(self, item, spider):
#         return item

class CraigslistImagePipeline:
    def process_item(self, item, spider):
        os.chdir('/home/higo/Documentos/Udemy/Scrapy: Powerful Web Scraping & Crawling with Python/craigslist/images')

        if not isinstance(item, CraigslistItem):
            return item
        
        if isinstance (item, CraigslistItem):
            if item['images'][0]['path']:
                path = item['images'][0]['path']
                path = path.replace('full/','/')
                txt = item['text'][0]
                r = slugify(txt)
                os.makedirs(r, exist_ok=True)
                new_path = r + path

                os.rename(item['images'][0]['path'], new_path)
                #os.rmdir('full')
