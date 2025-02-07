# romplinarena/scrapers/pipelines.py
from romplinarena.models import UFCEvent
from datetime import datetime

class DjangoPipeline:
    def process_item(self, item, spider):
        UFCEvent.objects.update_or_create(
            title=item['title'],
            defaults={
                'date': datetime.strptime(item['date'], '%B %d, %Y'),
                'location': item['location'],
                'event_url': item['event_url']
            }
        )
        return item
