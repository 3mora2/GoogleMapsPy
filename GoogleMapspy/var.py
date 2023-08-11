class Place:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Place(name={self.name}, phone={self.phone})"

    @property
    def name(self):
        return self.data[11]

    @property
    def phone(self):
        if self.data[178]:
            return self.data[178][0][3]
        elif self.data[3]:
            return self.data[3][0]

    @property
    def reviews(self) -> dict:
        if self.data[4]:
            return {
                "reviews_url": self.data[4][3][0],
                "reviews_count:str": self.data[4][3][1],
                "reviews_count:int": self.data[4][8],
            }
        return {}

    @property
    def expensive(self):
        return self.data[4][2] if self.data[4] else None

    @property
    def rate(self):
        return self.data[4][7] if self.data[4] else None

    @property
    def website(self) -> dict:
        if self.data[7]:
            return {
                "url": self.data[7][0],
                "title": self.data[7][1],
            }
        return {}

    @property
    def location(self) -> dict:
        if self.data[9]:
            return {
                "latitude": self.data[9][2],
                "longitude": self.data[9][3],
            }
        return {}

    @property
    def category(self) -> list:
        return self.data[13]

    @property
    def type2(self) -> list:
        return self.data[76]

    @property
    def address(self) -> dict:
        return {
            "split_address:list": self.data[2],
            "full": self.data[18],
            "full_split:list": self.data[183][0][0],
            "address": self.data[39],
            "district": self.data[14],
            "continent": self.data[30],
            "address_split:list": self.data[82],
            "address_country_city:str": self.data[166],
            "all_address_list": self.data[183]
        }

    @property
    def images(self) -> dict:
        return {
            "main": self.data[37][0][0][6][0]
        }

    @property
    def tags(self):
        return self.data[100]

    @property
    def short_tags(self):
        return self.data[142]

    @property
    def language(self):
        return self.data[107]

    @property
    def language_code(self):
        return self.data[110]

    @property
    def search_google_url(self):
        return self.data[174]

    @property
    def google_place_id(self):
        return self.data[78]

    @property
    def review_ids(self):
        return self.data[37][0][0][29]

    @property
    def url(self):
        return self.data[42]

    @property
    def days(self):
        d = []
        for day in self.data[203][0]:
            var = {"day_name": day[0], "day_id": day[1], "date": day[2],
                   "from_to": {"text": day[3][0][0], "from": day[3][0][1][0][0], "to": day[3][0][1][1][0]}}
            d.append(var)
        return d

    def json(self):
        return {
            "expensive": self.expensive,
            "reviews": self.reviews,
            "rate": self.rate,
            "website": self.website,
            "location": self.location,
            "name": self.name,
            "category": self.category,
            "type2": self.type2,
            "address": self.address,
            "images": self.images,
            "tags": self.tags,
            "short_tags": self.short_tags,
            "lang": self.language,
            "lang_code": self.language_code,
            "search_google_url": self.search_google_url,
            "phone": self.phone,
            "google_place_id": self.google_place_id,
            "review_ids": self.review_ids,
            "url": self.url,
            "days":self.days,
        }


class Review:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Review(contrib_name={self.contrib_name}, review={self.review[:500]})"

    @property
    def contrib_url(self):
        return self.data[0][0]

    @property
    def contrib_name(self):
        return self.data[0][1]

    @property
    def contrib_profile(self):
        return self.data[0][2]

    @property
    def contrib_level(self):
        return self.data[12][0][0] if self.data[12][0] else None

    @property
    def contrib_reviews_count(self):
        return self.data[12][1][1]

    @property
    def contrib_rate_count(self):
        return self.data[12][1][7]

    @property
    def create_at(self):
        return self.data[1]

    @property
    def review(self):
        if self.data[3]:
            return self.data[3]

        return ''

    @property
    def rate(self):
        return self.data[4]

    @property
    def review_url(self):
        return self.data[18]

    @property
    def lang(self):
        return self.data[32]

    @property
    def place_name(self):
        return self.data[14][0][21][3][7][1] if self.data[14] else None

    @property
    def likes(self):
        return self.data[16]

    @property
    def id(self):
        return self.data[61] if len(self.data) > 61 else None

    def json(self):
        return {
            "contrib_url": self.contrib_url,
            "contrib_name": self.contrib_name,
            "contrib_profile": self.contrib_profile,
            "contrib_level": self.contrib_level,
            "contrib_reviews_count": self.contrib_reviews_count,
            "contrib_rate_count": self.contrib_rate_count,
            "create_at": self.create_at,
            "review": self.review,
            "rate": self.rate,
            "review_url": self.review_url,
            "lang": self.lang,
            "place_name": self.place_name,
            "likes": self.likes,
            "id": self.id,

        }
