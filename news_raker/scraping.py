from .models import Source
import logging

logger = logging.getLogger(__name__)

def scrape_sources(*args, **kwargs):
    sources = Source.get_all()
    urls = sources['url'].tolist()
    for url in urls:
        print(url)
