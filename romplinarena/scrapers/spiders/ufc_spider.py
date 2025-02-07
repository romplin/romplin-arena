# romplinarena/scrapers/spiders/ufc_spider.py
import scrapy
from datetime import datetime
from romplinarena.models import UFCEvent

class UFCSpider(scrapy.Spider):
    name = 'ufc'
    start_urls = ['https://www.ufc.com/events']

    def parse(self, response):
        for event in response.css('div.c-card-event--result__info'):
            yield {
                'title': event.css('h3::text').get().strip(),
                'date': event.css('.date-display-single::text').get().strip(),
                'location': event.css('.field-content::text').get().strip(),
                'event_url': response.urljoin(event.css('a::attr(href)').get())
            }
