from .models import Source
import logging
import requests
from serp_bot import RequestDispatcher

logger = logging.getLogger(__name__)

dispatcher = RequestDispatcher()

def parse_xml(content):
    print('xml')
    print(content)

def parse_html(content):
    print('html')
    print(content)

def parse_others(content):
    print('others')
    print(content)

def fetch_and_determine_type(source): # Needs to be a part of bot identification logic
    content = dispatcher.get(source[1]['url'])
    if 'xml' in content.text[:20]:
        return 'xml', content.text
    elif 'html' in content.text[:20]:
        return 'html', content.text
    else:
        return 'other', content.text

def scrape_sources(*args, **kwargs):
    sources = Source.get_all()
    parse = {
        'xml' : parse_xml,
        'html' : parse_html,
        'others' : parse_others
    }
    for source in sources.iterrows():
        type, content = fetch_and_determine_type(source)
        parse[type](content)
