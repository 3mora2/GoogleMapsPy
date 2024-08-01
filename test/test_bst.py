from GoogleMapspy import GoogleMaps

import logging

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
text = "سوبرماركت في جدة"

old = []

maps = GoogleMaps(lang="ar", country_code="sa")
# for index, place in enumerate(maps.search(text, sleep_time=6, ), 1):
#
#     if place.hex_ids in old:
#         print(index, "find")
#         continue
#
#     old.append(place.hex_ids)
#     print(index, len(old), place)
# print(index, len(old))
url = "https://www.google.com/maps/place/%D8%A8%D9%8A%D8%AA%D8%B2%D8%A7+%D8%A5%D8%B3%D9%83%D9%86%D8%AF%D8%B1%D9%8A%D8%A9%E2%80%AD/@30.5890628,31.5035194,15.25z/data=!4m6!3m5!1s0x14f7f1aaacd1b6ab:0x9537d45cb200e0ee!8m2!3d30.5889755!4d31.4919853!16s%2Fg%2F1tj70ytd?entry=ttu"
p = maps.get_place(url=url)
print(p)
# 175
# 175 173
# 175 174
# 175 168


"""
{4: {'id': 4,
     'length': 6,
     'type': 'matrix',
     'value': {3: {'id': 3,
                   'length': 5,
                   'type': 'matrix',
                   'value': {1: {'id': 1,
                                 'type': 'string',
                                 'value': '0x14f7f1aaacd1b6ab:0x9537d45cb200e0ee'},
                             8: {'id': 8,
                                 'length': 2,
                                 'type': 'matrix',
                                 'value': {3: {'id': 3,
                                               'type': 'double',
                                               'value': 30.5889755},
                                           4: {'id': 4,
                                               'type': 'double',
                                               'value': 31.4919853}}},
                             16: {'id': 16,
                                  'type': 'string',
                                  'value': '/g/1tj70ytd?entry=ttu'}}}}}}
"""