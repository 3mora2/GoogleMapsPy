from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")

# keyword = "مطعم في الرياض  و جدة"
# for index, place in enumerate(maps.search(keyword)):
#     print(index, place.name, place.phone)
#
# places = maps.search(keyword, streem=False, sleep_time=0)
# print(places)
place_name = "مطعم الكتكوت للمشويات"
place = maps.get_place(place_name)
print(place.name)
# ids = ["1511502518116541527", "2022987617800227988"]
# for i, v in enumerate(maps.get_reviews(*ids, sleep_time=1)):
#     print(i, v.json())
("https://www.google.com/maps/place/{name}/@{31.3279843},{31.7535306},{17}z/data="
 "!3m1!4b1!4m6!3m5!1s0x14f9e7860c2edadf:0xe7ee7daab22713f!8m2!3d{31.3279843}!4d{31.7535306}!16s%2Fg%2F11rn4ndyt8?authuser=0&hl=ar&entry=ttu")
