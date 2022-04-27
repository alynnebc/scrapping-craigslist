import scrapy
from craigslist.items import CraigslistItem, CraigslistNoImageItem

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/egr']

    def parse(self, response):
        listings = response.xpath('//li[@class="result-row"]')

        for listing in listings:
            date = listing.xpath('.//time[@class="result-date"]/@datetime').extract_first()
            link = listing.xpath('.//h3/a/@href').extract_first()
            text = listing.xpath('.//h3/a/text()').extract_first()

            yield scrapy.Request(link,callback=self.parse_listing,meta={'date': date,
                                                                        'link': link,
                                                                        'text': text})
        
        next_page_url = response.xpath('//*[@class="button next"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
    
    def parse_listing(self, response):

        date = response.meta['date']
        link = response.meta['link']
        text = response.meta['text']

        compensation = response.xpath('//*[@class="attrgroup"]/span[contains(.,"compensation")]/b/text()').extract_first()
        employment_type = response.xpath('//*[@class="attrgroup"]/span[contains(.,"employment type")]/b/text()').extract_first()

        lat = response.xpath('//div[@class="mapbox"]/div/@data-latitude').extract_first()
        long = response.xpath('//div[@class="mapbox"]/div/@data-longitude').extract_first()

        description = response.xpath('//section[@id="postingbody"]/text()').extract()

        image_thumbs = response.xpath('//div[@id="thumbs"]/a/@href').extract()
        image_swipe_wrap = response.xpath('//div[@class="swipe-wrap"]/div/img/@src').extract()

        for image_t in image_thumbs:
                yield scrapy.Request(image_t,callback=self.parse_images,meta={'image': image_t,
                                                                            'date': date,
                                                                            'link': link,
                                                                            'compensation': compensation,
                                                                            'employment_type': employment_type,
                                                                            'lat': lat,
                                                                            'long': long,
                                                                            'description': description,
                                                                            'text': text})
        for image_s in image_swipe_wrap:
                yield scrapy.Request(image_s,callback=self.parse_images,meta={'image': image_s,
                                                                            'date': date,
                                                                            'link': link,
                                                                            'compensation': compensation,
                                                                            'employment_type': employment_type,
                                                                            'lat': lat,
                                                                            'long': long,
                                                                            'description': description,
                                                                            'text': text})

        yield CraigslistNoImageItem(date=[date], link=[link], text=[text], compensation=[compensation], employment_type=[employment_type],
        lat=[lat], long=[long], description=[description])
        #yield CraigslistItem()

        
    
    def parse_images(self, response):

        text = response.meta['text']
        image_urls = response.meta['image']

        date = response.meta['date']
        link = response.meta['link']
        compensation = response.meta['compensation']
        employment_type = response.meta['employment_type']
        lat = response.meta['lat']
        long = response.meta['long']
        description = response.meta['description']

        yield CraigslistItem(image_urls=[image_urls], date=[date], link=[link], text=[text], compensation=[compensation],
        employment_type=[employment_type], lat=[lat], long=[long], description=[description])