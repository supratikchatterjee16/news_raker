import os
import re
import json
import pandas

# Do not invoke logger in this file. It is meant to be an auxilliary standalone utility.

LIB_DIRECTORY, _ = os.path.split(__file__)
DATA_DIRECTORY = os.path.join(LIB_DIRECTORY, 'data')


def extract_domain_name(url):
    '''
    For extracting domain names.
    Given a FQDN, ex : https://www.sample.com/sub1/sub2
    We wish to extract 'sample'
    @params url(String)
    @returns domain_name(String)
    @author Supratik Chatterjee
    '''
    tld = pandas.read_csv(os.path.join(DATA_DIRECTORY, 'top_level_domains_2021061300.csv'))
    domain_name, root_domain  = None, None
    ctr = 0
    parts = re.findall('\w+', url)
    # print(parts)
    for part in parts:
        # if tld['Domains'].str.contains(part.upper()).any():
        root_domain = part
        if root_domain in ['com', 'net', 'org']:
            break
        domain_name = part
        ctr += 1
    if ctr == len(parts):
        return None
    return domain_name+'.'+root_domain

def pretty_print(x):# pretty print dictionaries
    '''
    Helps print a dictionary. Using the json library
    @params dict
    @returns None
    @author Supratik Chatterjee
    '''
    print('\n', json.dumps(x, indent=4, sort_keys=True), '\n')
# class FileBroker(dict):
#     def __init__(self):
#         self.directory = None
#         self.files = {}
#         self.subfolders = {}
#     def mount(self, dir):
#         if not os.path.isdir(dir):
#             raise ValueError("Incorrect entry as a directory :", dir)
#         self.directory = os.path.abspath(dir)
#         for entry in os.listdir(self.directory):
#             current_entry = os.path.join(self.directory, entry)
#             if os.path.isfile(current_entry):
#                 self.files[entry.split('.')[0]] = entry
#
#      def __setitem__(self, key, item):
#         self.__dict__[key] = item
#
#     def __getitem__(self, key):
#         return self.__dict__[key]
#
#     def __repr__(self):
#         return repr(self.__dict__)
#
#     def __len__(self):
#         return len(self.__dict__)
#
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
#     def clear(self):
#         return self.__dict__.clear()
#
#     def copy(self):
#         return self.__dict__.copy()
#
#     def has_key(self, k):
#         return k in self.__dict__
#
#     def update(self, *args, **kwargs):
#         return self.__dict__.update(*args, **kwargs)
#
#     def keys(self):
#         return self.__dict__.keys()
#
#     def values(self):
#         return self.__dict__.values()
#
#     def items(self):
#         return self.__dict__.items()
#
#     def pop(self, *args):
#         return self.__dict__.pop(*args)
#
#     def __cmp__(self, dict_):
#         return self.__cmp__(self.__dict__, dict_)
#
#     def __contains__(self, item):
#         return item in self.__dict__
#
#     def __iter__(self):
#         return iter(self.__dict__)
#
#     def __unicode__(self):
#         return unicode(repr(self.__dict__))
