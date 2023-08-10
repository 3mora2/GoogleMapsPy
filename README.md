# GoogleMapsPY

GoogleMapsPY aim to scrape data from Google Maps without Google API


## Functions

|                          |   |
|--------------------------|---|
| Search and return Places | ✔ |
| Get Place by name        | ✔ |
| Get Reviews              | ✔ |
|                          |   |


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

`place_name` must be accurate
```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
place_name = "مطعم الكتكوت للمشويات، مدينة الروضة، مركز فارسكور"
place = maps.get_place(place_name)
print(place)
```

### Get Reviews
pass ids
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
or google maps place url
```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
url = "https://www.google.com/maps/place/%D9%86%D8%A7%D8%AF%D9%8A+%D8%A7%D9%84%D9%85%D9%87%D9%86%D8%AF%D8%B3%D9%8A%D9%86+%D8%AF%D9%85%D9%8A%D8%A7%D8%B7+%D8%A7%D9%84%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9%E2%80%AD/@31.4438138,31.7206443,14.44z/data=!4m6!3m5!1s0x14f9e3054ae0727f:0xde8f78c8fa6ac846!8m2!3d31.4519438!4d31.6843306!16s%2Fg%2F1pty8slyq?entry=ttu"
for i, v in enumerate(maps.get_reviews(url=url, sleep_time=1)):
    print(i, v)
```