import os.path
from datetime import datetime

from GoogleMapspy import GoogleMaps
import pandas

file_save = os.path.join(f'Google Map - {datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.xlsx')
maps = GoogleMaps(lang="ar", country_code="eg")

keyword = "مطعم في الرياض"
places = []
for index, place in enumerate(maps.search(keyword)):
    print(index, place)
    places.append(
        {
            "name": place.name,
            "category": place.category,

            "type": place.type,
            "subtypes": ", ".join(place.subtypes),

            "phone": place.phone,
            "phone_format": place.phone_format,
            "description": place.description,
            "district": place.district,
            "street": place.street,
            "city": place.city,
            "postal_code": place.postal_code,
            "plus_code": place.plus_code,
            "country_code": place.country_code,
            "rate": place.rate,
            "expensive": place.expensive,
            "reviews": place.reviews,
            "site_url": place.site_url,
            "site_text": place.site_text,

            "full_address_name": place.full_address_name,
            "location": place.location,
            "url": place.url,
            "main_image": place.main_image,
            "lang": place.language,
            "lang_code": place.language_code,
            "search_google_url": place.search_google_url,
            "google_place_id": place.google_place_id,
            "type2": place.type2,
            "website": place.website.get("url"),
            "tags": place.tags,
            "short_tags": place.short_tags,
            "days": place.days,
        }
    )

pandas.DataFrame(places).to_excel(file_save, index=False)
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