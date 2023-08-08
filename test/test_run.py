from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")

keyword = "مطعم في الرياض"
for index, place in enumerate(maps.search(keyword)):
    print(index, place.name, place.phone)

places = maps.search(keyword, streem=False, sleep_time=0)
