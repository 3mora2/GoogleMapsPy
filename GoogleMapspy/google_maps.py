import json
from time import sleep
from geopy.geocoders import Nominatim
from fake_useragent import UserAgent
from requests_html import HTMLSession
from GoogleMapspy.function import get_1d
from GoogleMapspy.var import Place

ua = UserAgent()


class GoogleMaps:

    def __init__(self, latitude: str = "", longitude: str = "", lang: str = "ar", country_code: str = "eg",
                 offset: int = 0, p: int = 20, zoom=None, zoom_index=9):
        self.latitude = latitude
        self.longitude = longitude
        self.offset = offset
        self.p = p
        self.keyword = ""
        self.zoom = zoom or get_1d(0).get(zoom_index)
        self.hl = lang
        self.gl = country_code
        self.session = HTMLSession()
        self.Places = []

    def search(self, keyword, all_=True, clear_old=True, offset=0, p=20, streem=True, sleep_time: int = 5):
        self.offset = offset
        self.p = p
        if clear_old:
            self.Places = []
        self.keyword = keyword

        if not self.latitude or not self.longitude:
            self.__set_latitude(keyword)

        while True:
            r = self.session.request("GET", self._url_search, headers=self.headers)
            r.raise_for_status()

            list_data = json.loads(r.text[5:])

            # check if there data
            if len(list_data[0][1][1:]) == 0:
                break

            for ll in list_data[0][1][1:]:
                place = Place(ll)
                self.Places.append(place)
                if streem:
                    yield place
                # print(len(self.Places), place.name, place.phone)

            if not all_:
                break
            self.offset += 20
            sleep(sleep_time)

        return self.Places

    def __set_latitude(self, keyword):
        geolocator = Nominatim(user_agent=ua.random)
        location = geolocator.geocode(keyword)
        self.latitude = location.latitude
        self.longitude = location.longitude

    @property
    def headers(self):
        return {
            "accept": "*/*",
            "referrer": "https://www.google.com/",
            "User-Agent": ua.random
        }

    @property
    def _url_search(self):
        return (
            f"https://www.google.com/search?tbm=map&authuser=0&hl={self.hl}&gl={self.gl}&q={self.keyword}&oq={self.keyword}&"
            f"pb=!4m12!1m3!1d{self.zoom}!2d{self.longitude}!3d{self.latitude}!2m3!1f0!2f0!3f0!3m2!1i1536!2i686!4f13.1!7i{self.p}!8i{self.offset}"
            "!10b1!12m16!1m1!18b1!2m3!5m1!6e2!20e3!10b1!12b1!13b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!19m4!2m3!1i360!2i120!4i8"
            "!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3"
            "!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2"
            "!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1stRLSZM7lG--0kdUPh8SyiAM%3A4!2s1i%3A0%2Ct%3A11886%2Cp%3AtRLSZM7lG"
            "--0kdUPh8SyiAM%3A4!7e81!12e5!17stRLSZM7lG--0kdUPh8SyiAM%3A28!18e15!24m81!1m29!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1"
            "!20b1!25b1!18m18!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!25b1!27m1!1b0!28b0!30b0!2b1!5m5!2b1"
            "!5b1!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1"
            "!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!103b1"
            "!113b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i50!2i686!1m6!1m2!1i1006!2i0!2m2!1i1536!2i686!1m6!1m2"
            "!1i0!2i0!2m2!1i1536!2i20!1m6!1m2!1i0!2i666!2m2!1i1536!2i686!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1"
            "!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!47m0!49m7!3b1!6m2!1b1!2b1!7m2!1e3!2b1!50m4!2e2!3m2!1b1!3b1"
            "!61b1!67m2!7b1!10b1!69i657"
        )
