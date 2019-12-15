import scrapy
import pickle
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import TakeFirst, MapCompose, Join

from immoscout.items import ObjectItem
from datetime import date

filename = "immoScoutListings.txt"



class GRSpider(scrapy.Spider):
    name = "immoSpider"
    allowed_domains = [ 'immobilienscout24.com']

    def __init__(self, domain=None, *args, **kwargs):
                self.domain = domain

    def start_requests(self):
        urls = [self.domain]
        # We generate a Request for each URL
        # We also specify the use of the parse function to parse the responses
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Define how to handle the response object in the parse function
    # Here, we extract the the elements of the listing and write it to a file        
    def parse(self, response):
        
        # Extract the property elements
        immoListing  = response.css('div.content-wrapper')
        object_loader = ItemLoader(item=ObjectItem(), selector=immoListing)
        object_loader.default_output_processor = TakeFirst()
        object_loader.add_css('title', 'h1::text')
        object_loader.add_css('address', 'div.address-block > div > span::text')
        
        #write to file using pickle, to get nicer format from ItemLoader object
        #with open(filename, 'wb') as f:
        #    pickle.dump(object_loader, f)

        yield object_loader.load_item() 

