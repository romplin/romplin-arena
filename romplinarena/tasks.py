# my_project/my_app/tasks.py
from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import ScrapedData

@shared_task
def scrape_website():
    # Your scraping logic here
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: save scraped data
    ScrapedData.objects.create(
        title=soup.find('h1').text,
        content=soup.find('div', class_='content').text
    )
