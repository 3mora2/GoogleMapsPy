from requests_html import HTMLSession
from fake_useragent import UserAgent
from geopy.geocoders import Nominatim


ua = UserAgent()
session = HTMLSession()
word = "الرياض"


geolocator = Nominatim(user_agent=ua.random)
location = geolocator.geocode(word)
location.latitude
location.longitude


# "https://www.google.com.hk/maps/place/{place}/@0,0,0z/data=!4m5!3m4!1s{longitude}!8m2!3d{latitude}!4d{location_code}"
# url = f"https://www.google.com/maps/place/{word}/@0,0,0z"
#
# headers = {
#     "accept": "*/*",
#     "referrer": "https://www.google.com/",
#     "User-Agent": ua.random
# }
# r = session.get( url, headers=headers)
