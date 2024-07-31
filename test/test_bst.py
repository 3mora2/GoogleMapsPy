from GoogleMapspy import GoogleMaps

import logging

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
text = "سوبرماركت في جدة"

old = []

maps = GoogleMaps(lang="ar", country_code="sa")
for index, place in enumerate(maps.search(text, sleep_time=6, ), 1):

    if place.hex_ids in old:
        print(index, "find")
        continue

    old.append(place.hex_ids)
    print(index, len(old), place)
print(index, len(old))
# 175
# 175 173
# 175 174
# 175 168
