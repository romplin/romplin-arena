# romplinarena/scrapers/settings.py
import os
import sys
import django

# Add Django project to path
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'romplinarena.settings'
django.setup()

# Scrapy settings
BOT_NAME = 'scrapers'

SPIDER_MODULES = ['romplinarena.scrapers.spiders']
NEWSPIDER_MODULE = 'romplinarena.scrapers.spiders'

ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 2

ITEM_PIPELINES = {
    'romplinarena.scrapers.pipelines.DjangoPipeline': 300,
}
