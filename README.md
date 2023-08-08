# GoogleMapsPY

GoogleMapsPY aim to scrape data from Google Maps without Google API


## Functions

|                          |   |
|--------------------------|---|
| Search and return Places | ✔ |
|                          |   |


### Installation
```
pip install git+https://www.github.com/3mora2/GoogleMapsPy@main
```

### Search Keyword
```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
keyword = "مطعم في الرياض"
for index, place in enumerate(maps.search(keyword)):
    print(index, place.name, place.phone)
```
or
```python
from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")
keyword = "مطعم في الرياض"
places = maps.search(keyword, streem=False, sleep_time=0)
print(places)

# print place data as json
print(places[0].json())
```

`lang` is language like ( "ar", "en", ...)
`country_code` from [country_suffix_dict](https://www.github.com/3mora2/GoogleMapsPy/GoogleMapsPy/const.py)