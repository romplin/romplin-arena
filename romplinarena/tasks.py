# tasks.py
from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .scrapers.spiders.ufc_spider import UFCSpider

@shared_task
def scrape_ufc_events():
   process = CrawlerProcess(get_project_settings())
   process.crawl(UFCSpider)
   process.start()
