import re
import requests

from .utils import extract_domain_name, pretty_print
def scan(url, **kwargs):
    '''
    Fetch all identifiable links within the same domain.
    @params url
    @returns filtered dictionary of URLs from the same domain
    @author Supratik Chatterjee
    '''
    page = requests.get(url)
    # pre-formatting for al-jazeera
    domain_name = extract_domain_name(url)
    anchor_regex = "<a.*?/a>"# no adjust
    href_regex = "href=\"\S*\"" # adjust [6: -1]
    anchor_title_regex = ">[A-Za-z0-9\-&;|\', ]+<" # adjust [1 : -4]
    anchors = re.findall(anchor_regex, page.text)
    urls = {}
    # print("Domain name : ", domain_name)
    for anchor in anchors:
        # print(anchor)
        href = re.findall(href_regex, anchor)
        titles = re.findall(anchor_title_regex, anchor)
        # print(href, titles, len(href), len(titles))
        if len(href) > 0 and len(titles) > 0:
            adjusted_href = href[0][6: -1]
            adjusted_title = titles[0][1:-1]
            # print(adjusted_title, adjusted_href)
            if adjusted_href.startswith('http'):
                if domain_name in adjusted_href:
                    urls[adjusted_title] = adjusted_href
            else:
                urls[adjusted_title] = url + (adjusted_href[1:] if adjusted_href.startswith('/') else adjusted_href)
    if 'supervised_filtration' in kwargs:
        if kwargs['supervised_filtration']:
            filter_str = input("String to use to filter further(based on URLs) : ")
            filtered = {k:v for k,v in urls.items() if filter_str in v}
            # pretty_print(filtered)
            return filtered
    if 'debug' in kwargs:
        if kwargs['debug']:
            pretty_print(urls)
    return urls
