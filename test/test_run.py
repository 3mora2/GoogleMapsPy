from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="ar", country_code="eg")

# keyword = "مطعم في الرياض"
# for index, place in enumerate(maps.search(keyword)):
#     print(index, place)
#
# places = maps.search(keyword, streem=False, sleep_time=0)
# print(places)

# place_name = "مطعم الكتكوت للمشويات، مدينة الروضة، مركز فارسكور"
# place = maps.get_place(place_name)
# print(place)
#
# d = maps.get_images(place.review_ids)
# print(d)
# ids = place.review_ids  # ["1511502518116541527", "2022987617800227988"]
# for i, v in enumerate(maps.get_reviews(ids=ids, sleep_time=1)):
#     print(i, v)
#
# url = "https://www.google.com/maps/place/%D9%86%D8%A7%D8%AF%D9%8A+%D8%A7%D9%84%D9%85%D9%87%D9%86%D8%AF%D8%B3%D9%8A%D9%86+%D8%AF%D9%85%D9%8A%D8%A7%D8%B7+%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9%E2%80%AD/@31.4438138,31.7206443,14.44z/data=!4m6!3m5!1s0x14f9e3054ae0727f:0xde8f78c8fa6ac846!8m2!3d31.4519438!4d31.6843306!16s%2Fg%2F1pty8slyq?entry=ttu"
# for i, v in enumerate(maps.get_reviews(url=url, sleep_time=1)):
#     print(i, v)

# url = "https://www.google.com/maps/place/%D9%83%D9%86%D8%AA%D8%A7%D9%83%D9%8A%E2%80%AD/@31.4398058,31.5456013,15.13z/data=!4m19!1m10!3m9!1s0x14f9e7860c2edadf:0xe7ee7daab22713f!2z2YXYt9i52YUg2KfZhNmD2KrZg9mI2Kog2YTZhNmF2LTZiNmK2KfYqg!8m2!3d31.3279843!4d31.7535306!10e5!14m1!1BCgIgAQ!16s%2Fg%2F11rn4ndyt8!3m7!1s0x14f75c007d47ea73:0xab691d2a3fba4d12!8m2!3d31.4412519!4d31.5342442!9m1!1b1!16s%2Fg%2F11g8gl1n55?entry=ttu"
# place = maps.get_place(url=url)
# print(place)