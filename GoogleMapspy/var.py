class Place:
    def __init__(self, data):
        self.data = data

    @property
    def name(self):
        return self.data[14][11]

    @property
    def phone(self):
        if self.data[14][178]:
            return self.data[14][178][0][3]
        elif self.data[14][3]:
            return self.data[14][3][0]

    @property
    def reviews(self) -> dict:
        if self.data[14][4]:
            return {
                "reviews_url": self.data[14][4][3][0],
                "reviews_count:str": self.data[14][4][3][1],
                "reviews_count:int": self.data[14][4][8],
            }
        return {}

    @property
    def expensive(self):
        return self.data[14][4][2] if self.data[14][4] else None

    @property
    def rate(self):
        return self.data[14][4][7] if self.data[14][4] else None

    @property
    def website(self) -> dict:
        if self.data[14][7]:
            return {
                "url": self.data[14][7][0],
                "title": self.data[14][7][1],
            }
        return {}

    @property
    def location(self) -> dict:
        if self.data[14][9]:
            return {
                "latitude": self.data[14][9][2],
                "longitude": self.data[14][9][3],
            }
        return {}

    @property
    def category(self) -> list:
        return self.data[14][13]

    @property
    def type2(self) -> list:
        return self.data[14][76]

    @property
    def address(self) -> dict:
        return {
            "split_address:list": self.data[14][2],
            "full": self.data[14][18],
            "full_split:list": self.data[14][183][0][0],
            "address": self.data[14][39],
            "district": self.data[14][14],
            "continent": self.data[14][30],
            "address_split:list": self.data[14][82],
            "address_country_city:str": self.data[14][166],
            "all_address_list": self.data[14][183]
        }

    @property
    def images(self) -> dict:
        return {
            "main": self.data[14][37][0][0][6][0]
        }

    @property
    def tags(self):
        return self.data[14][100]

    @property
    def short_tags(self):
        return self.data[14][142]

    @property
    def language(self):
        return self.data[14][107]

    @property
    def language_code(self):
        return self.data[14][110]

    @property
    def search_google_url(self):
        return self.data[14][174]

    @property
    def google_place_id(self):
        return self.data[14][78]

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
            "google_place_id": self.google_place_id
        }
