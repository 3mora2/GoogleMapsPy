import json
import re
from time import sleep
from geopy.geocoders import Nominatim
from fake_useragent import UserAgent
from requests_html import HTMLSession
from GoogleMapspy.function import get_1d, country_suffix_dict
from GoogleMapspy.var import Place, Review
from urllib.parse import quote
from urllib.parse import urlparse, parse_qs, unquote

ua = UserAgent()


class GoogleMaps:

    def __init__(self, latitude: str = "", longitude: str = "", lang: str = "en", country_code: str = "eg", zoom=None,
                 zoom_index=9):
        self.latitude = latitude
        self.longitude = longitude
        self.keyword = ""
        self.place_name = ""
        self.zoom = zoom or get_1d(0).get(zoom_index)
        self.hl = lang
        self.gl = country_code
        self.session = HTMLSession()
        self.places = []
        self.reviews = []

    def get_images(self, ids=[]):
        if ids:
            id1, id2 = ids
        else:
            raise
        self.__set_latitude()
        r = self.session.request("GET", self._get_images_url(id1_=id1, id2_=id2), headers=self.headers)
        r.raise_for_status()
        list_data = json.loads(r.text[5:])
        images = []
        l = []
        for image in list_data[0]:
            l.append(image[6][0])
        var = {"name": "all_image", "images": l}
        images.append(var)

        for cat in list_data[12][0]:
            l = []
            for image in cat[3]:
                if len(image) > 6:
                    l.append(image[6][0])
            var = {"name": cat[2], "images": l}
            images.append(var)

        return images

    def get_reviews(self, ids=[], url="", clear_old=True, streem=True, sleep_time: int = 5):
        if ids:
            id1, id2 = ids
        elif url:
            id1, id2 = self.__get_ids_from_url(url)
            if not id1:
                raise Exception("not valid url")
        else:
            raise Exception("pass ids or url")

        self.reviews = []
        last_id = ""
        self.__set_latitude()
        tr = True
        while tr:
            r = self.session.request("GET", self._url_get_review(id1, id2, last_id), headers=self.headers)
            r.raise_for_status()
            list_data = json.loads(r.text[5:])

            if len(list_data[2]) == 0:
                break

            for ll in list_data[2]:
                review = Review(ll)
                last_id = review.id
                self.reviews.append(review)
                if streem:
                    yield review
                if not last_id:
                    tr = False
                    break

            sleep(sleep_time)
        return self.reviews

    @staticmethod
    def __get_ids_from_url(url, hex_=False):
        if not hex_:
            res = re.findall(r"1s(\w+):(\w+)!", url)

            if res:
                return [int(res[0][0], 16), int(res[0][1], 16)]
            return ["", ""]
        else:
            res = re.findall(r"s(\w+:\w+)!", url)
            if res:
                return res[0]

    @staticmethod
    def __get_name_from_url(url):
        res = re.findall(r"/place/(.*)/@", url)
        if res:
            return res[0]
        return ""

    def get_place(self, keyword="", url="", offset=0, p=100):
        self.__set_latitude(keyword)
        if keyword:
            r = self.session.request("GET", self._url_search(keyword, p, offset), headers=self.headers)
            r.raise_for_status()

            list_data = json.loads(r.text[5:])

            data, type_ = self.__prepare_data(list_data)
            if type_ == "place":
                place = Place(data[14])
            elif type_ == "list":
                place = Place(data[0][14])
            else:
                return None
        elif url:
            r = self.session.request("GET", self._url_get_place(url), headers=self.headers)
            r.raise_for_status()

            list_data = json.loads(r.text[5:])
            place = Place(list_data[6])
        else:
            raise

        return place

    @staticmethod
    def __prepare_data(data):
        if data[0][3] == 0 and len(data[0][1]) > 0:
            # print("place return ")
            return data[0][1][0], "place"
        elif data[0][3] == 1 and len(data[0][1][1:]):
            # print("search return list")
            return data[0][1][1:], 'list'
        return [], None

    def search(self, keyword, all_=True, clear_old=True, offset=0, p=100, streem=True, sleep_time: int = 5):
        if clear_old:
            self.places = []
        self.keyword = keyword

        if not self.latitude or not self.longitude:
            self.__set_latitude(keyword)

        while True:
            r = self.session.request("GET", self._url_search(keyword, p, offset), headers=self.headers)
            r.raise_for_status()

            list_data = json.loads(r.text[5:])
            data, type_ = self.__prepare_data(list_data)
            if type_ == "place":
                place = Place(data[14])
                self.places.append(place)
                yield place
                break

            elif type_ == "list":
                for ll in data:
                    place = Place(ll[14])
                    self.places.append(place)
                    if streem:
                        yield place
                    # print(len(self.Places), place.name, place.phone)

            else:
                break

            # # check if there data
            # if len(list_data[0][1][1:]) == 0:
            #     break

            if not all_:
                break
            offset += p
            sleep(sleep_time)

        return self.places

    def __set_latitude(self, keyword=""):
        geolocator = Nominatim(user_agent=ua.random)
        try:
            if keyword:
                location = geolocator.geocode(keyword)
                self.latitude = location.latitude
                self.longitude = location.longitude
            else:
                name = country_suffix_dict.get(self.gl)
                # if name:
                location = geolocator.geocode(name)
                self.latitude = location.latitude
                self.longitude = location.longitude
        except AttributeError as error:
            name = country_suffix_dict.get(self.gl)
            if name:
                location = geolocator.geocode(name)
                self.latitude = location.latitude
                self.longitude = location.longitude
            else:
                raise error

    @property
    def headers(self):
        return {
            "accept": "*/*",
            "referrer": "https://www.google.com/",
            "User-Agent": ua.random
        }

    def _url_search(self, keyword, p, offset):
        """
        :param keyword:
        :return:
        url:
            hl: language
            gl: country code
            q=oq: keyword

        """
        return (
            ""
            f"https://www.google.com/search?tbm=map&authuser=0&hl={self.hl}&gl={self.gl}&q={keyword}&oq={keyword}&"
            f"pb=!4m12!1m3!1d{self.zoom}!2d{self.longitude}!3d{self.latitude}!2m3!1f0!2f0!3f0!3m2!1i1536!2i686!4f13.1!7i{p}!8i{offset}"
            "!10b1!12m16!1m1!18b1!2m3!5m1!6e2!20e3!10b1!12b1!13b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!19m4!2m3!1i360!2i120!4i8"
            "!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3"
            "!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2"
            "!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1stRLSZM7lG--0kdUPh8SyiAM:4!2s1i:0,t:11886,p:tRLSZM7lG"
            "--0kdUPh8SyiAM:4!7e81!12e5!17stRLSZM7lG--0kdUPh8SyiAM:28!18e15!24m81!1m29!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1"
            "!20b1!25b1!18m18!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!25b1!27m1!1b0!28b0!30b0!2b1!5m5!2b1"
            "!5b1!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1"
            "!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!103b1"
            "!113b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i50!2i686!1m6!1m2!1i1006!2i0!2m2!1i1536!2i686!1m6!1m2"
            "!1i0!2i0!2m2!1i1536!2i20!1m6!1m2!1i0!2i666!2m2!1i1536!2i686!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1"
            "!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!47m0!49m7!3b1!6m2!1b1!2b1!7m2!1e3!2b1!50m4!2e2!3m2!1b1!3b1"
            "!61b1!67m2!7b1!10b1!69i657"
        )

    def _url_get_place(self, url):
        id1_id2 = self.__get_ids_from_url(url, hex_=True)
        if not id1_id2:
            raise Exception("not valid url")
        place_name = self.__get_name_from_url(url)
        return (
            f"https://www.google.com/maps/preview/place?authuser=0&hl={self.hl}&gl={self.gl}&q={quote(place_name)}&pb=!1m11!1s{id1_id2}!3m9!1m3"
            f"!1d{self.zoom}!2d{self.longitude}!3d{self.latitude}!2m0!3m2!1i1536!2i686!4f13.1!12m4!2m3!1i360!2i120!4i8!13m57!2m2"
            "!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3"
            "!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10"
            "!2b0!3e4!2b1!4b1!9b0!14m2!1sJavSZPiQCfGqkdUPx469kA4!7e81!15m82!1m30!4e2!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1"
            "!25b1!18m18!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!25b1!27m1!1b0!28b0!30b0!2b1!5m5!2b1!5b1"
            "!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1"
            "!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!103b1!113b1"
            "!21m28!1m6!1m2!1i0!2i0!2m2!1i50!2i686!1m6!1m2!1i1006!2i0!2m2!1i1536!2i686!1m6!1m2!1i0!2i0!2m2!1i1536!2i20!1m6"
            "!1m2!1i0!2i666!2m2!1i1536!2i686!22m1!1e81!29m0!30m5!3b1!6m1!2b1!7m1!2b1!34m2!7b1!10b1!37i657"
            "!39z2K3ZhNmI2YrYp9iqINin2YTYqNiv2LHZiiDZg9mI2LHZhtmK2LQg2KfZhNmG2YrZhA")

    def _url_get_review(self, id1, id2, last_id="", page=200):
        """
        :param id1:
        :param id2:
        :param last_id:
        :param page:
        :return:
        url
         hl: language
         gl: country code
         pb:
            1(2length):
                [
                    1: id1
                    2: id2
               ]
            2(length 1or2):
                [
                    2: page
                    3: last id
                ]
            ...
        """
        return (
            f"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl={self.hl}&gl={self.gl}&"
            f"pb=!1m2!1y{id1}!2y{id2}!{'2m2' if last_id else '2m1'}!2i{page}{('!3s' + last_id) if last_id else ''}!3e1!4m5!3b1!4b1!6b1!7b1!20b1!5m2!1sJavSZPiQCfGqkdUPx469kA4!7e81")

    def _get_images_url(self, id1_, id2_):
        return (
            f"https://www.google.com/maps/preview/photo?authuser=0&hl={self.hl}&gl={self.gl}&pb=!1e2!3m3!"
            f"1s{hex(int(id1_))}:{hex(int(id2_))}!9e0!11s/g/11rn4ndyt8!5m50!2m2!1i203!2i100!3m2!2i20!5b1!7m42!1m3!1e1!2b0!3e3!1m3!1e2"
            "!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0"
            "!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!6m3!1sfBnWZJe_L5GjkdUPnfi7-AQ!7e81!15i16698!16m2!2b1"
            "!4e1")
