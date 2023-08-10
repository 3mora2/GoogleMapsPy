from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")

# keyword = "مطعم في الرياض  و جدة"
# for index, place in enumerate(maps.search(keyword)):
#     print(index, place)
#
# places = maps.search(keyword, streem=False, sleep_time=0)
# print(places)
place_name = "مطعم الكتكوت للمشويات، مدينة الروضة، مركز فارسكور"
place = maps.get_place(place_name)
print(place)
ids = place.review_ids  # ["1511502518116541527", "2022987617800227988"]
for i, v in enumerate(maps.get_reviews(ids=ids, sleep_time=1)):
    print(i, v)

url = "https://www.google.com/maps/place/%D9%86%D8%A7%D8%AF%D9%8A+%D8%A7%D9%84%D9%85%D9%87%D9%86%D8%AF%D8%B3%D9%8A%D9%86+%D8%AF%D9%85%D9%8A%D8%A7%D8%B7+%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9%E2%80%AD/@31.4438138,31.7206443,14.44z/data=!4m6!3m5!1s0x14f9e3054ae0727f:0xde8f78c8fa6ac846!8m2!3d31.4519438!4d31.6843306!16s%2Fg%2F1pty8slyq?entry=ttu"
for i, v in enumerate(maps.get_reviews(url=url, sleep_time=1)):
    print(i, v)
