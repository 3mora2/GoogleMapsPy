# GoogleMapsPY

GoogleMapsPY aim to scrape data from Google Maps without Google API or Browser


## Functions

|                          |   |
|--------------------------|---|
| Search and return Places | ✔ |
| Get Place by name        | ✔ |
| Get Reviews              | ✔ |
| Get Images               |   |


### Installation
```
pip install git+https://www.github.com/3mora2/GoogleMapsPy@main
```

### Start

```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
```
`lang` is language like ( "ar", "en", ...)

`country_code` from [country_suffix_dict](https://github.com/3mora2/GoogleMapsPy/blob/dfb5cb24324fc5664a53591932ae5b05ab219c24/GoogleMapspy/const.py#L98)

### Search Keyword

```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
keyword = "مطعم في الرياض"
for index, place in enumerate(maps.search(keyword)):
    print(index, place)
```

### Get Place
by place_name
`place_name` must be accurate
```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
place_name = "مطعم الكتكوت للمشويات، مدينة الروضة، مركز فارسكور"
place = maps.get_place(place_name)
print(place)
```
or by google maps place url

```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
url = "https://www.google.com/maps/place/%D9%85%D8%B7%D8%B9%D9%85+%D8%A7%D9%84%D8%B5%D8%A7%D9%81%D9%89+%D8%A7%D9%84%D9%85%D8%A3%D9%83%D9%88%D9%84%D8%A7%D8%AA+%D8%A7%D9%84%D8%A8%D8%AD%D8%B1%D9%8A%D8%A9%E2%80%AD/@31.3236418,31.7580646,17z/data=!4m17!1m10!3m9!1s0x14f9e7860c2edadf:0xe7ee7daab22713f!2z2YXYt9i52YUg2KfZhNmD2KrZg9mI2Kog2YTZhNmF2LTZiNmK2KfYqg!8m2!3d31.3279843!4d31.7535306!10e5!14m1!1BCgIgAQ!16s%2Fg%2F11rn4ndyt8!3m5!1s0x14f9e72c1e2e1beb:0x656909fce8b20df!8m2!3d31.3237011!4d31.7580212!16s%2Fg%2F11hzjy_4bd?entry=ttu"
place = maps.get_place(url=url)
print(place)
```

### Get Reviews
by ids
```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
place_name = "مطعم الكتكوت للمشويات، مدينة الروضة، مركز فارسكور"
place = maps.get_place(place_name)
print(place)
ids = place.review_ids  # ["1511502518116541527", "2022987617800227988"]
for i, review in enumerate(maps.get_reviews(ids=ids)):
    print(i, review)
```
or by google maps place url
```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
url = "https://www.google.com/maps/place/%D9%86%D8%A7%D8%AF%D9%8A+%D8%A7%D9%84%D9%85%D9%87%D9%86%D8%AF%D8%B3%D9%8A%D9%86+%D8%AF%D9%85%D9%8A%D8%A7%D8%B7+%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9%E2%80%AD/@31.4438138,31.7206443,14.44z/data=!4m6!3m5!1s0x14f9e3054ae0727f:0xde8f78c8fa6ac846!8m2!3d31.4519438!4d31.6843306!16s%2Fg%2F1pty8slyq?entry=ttu"
for i, v in enumerate(maps.get_reviews(url=url, sleep_time=1)):
    print(i, v)
```

### Get Images
by ids
```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
place_name = "مطعم الكتكوت للمشويات، مدينة الروضة، مركز فارسكور"
place = maps.get_place(place_name)
print(place)
ids = place.review_ids  # ["1511502518116541527", "2022987617800227988"]
images = maps.get_images(ids)
print(images)
```


### Place object property:
| name              | type  | return                               |
|-------------------|-------|--------------------------------------|
| expensive         | str   | expensive level                      |
| reviews           | dict  | reviews url, count                   |
| rate              | float | rate                                 |
| website           | dict  | website url                          |
| location          | dict  | location dict of latitude, longitude |
| name              | str   | name of place                        |
| category          | list  | category                             |
| type2             | list  | type2                                |
| address           | dict  | address                              |
| images            | dict  | images (main image)                  |
| tags              | list  | tags                                 |
| short_tags        | list  | short_tags                           |
| lang              | str   | language                             |
| lang_code         | str   | language_code                        |
| search_google_url | str   | search_google_url                    |
| phone             | str   | phone                                |
| google_place_id   | str   | google_place_id                      |
| review_ids        | list  | review_ids                           |
| url               | str   | url                                  |
| days              | list  | open in days                         |
