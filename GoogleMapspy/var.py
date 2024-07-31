def get_index(data: list, *args, default=None):
    val = data
    for index in args:
        if val is None or len(val) <= index:
            return default
        val = val[index]
    return val


class Place:
    def __init__(self, data):
        """
        Index 2>0: street
        Index 2>1: district
        Index 2>2: city
        Index 2>3: ... last part address

        Index 3: phones ???

        Index 4: reviews
        Index 4>2: expensive
        Index 4>3: reviews url, text, ...
        Index 4>7: rating
        Index 4>8: reviews_count
        Index 4>10: expensive text


        Index 7: site
        Index 7>0: site url
        Index 7>1: site title

        Index 9: latitude(9>2),longitude(9>3)
        Index 10: google_id, hex_ids
        Index 11: name
        Index 13 > 0: type
        Index 13: subtypes list 'Pizza restaurant', 'Fast food restaurant', 'Restaurant']
        Index 14: district
        Index 18: full address + name
        Index 30: Time Zone: 'Asia/Riyadh'
        Index 32>1>1: description
        Index 33: Service Options
        Index 34>1: working_hours

        Index 37>0: images
        Index 37>0>0>29: review_ids
        Index 37>1: photos_count

        Index 39: full_address
        Index 42: url
        Index 52>3: reviews_per_score

        Index 57: owner(https://www.google.com/maps/contrib/owner_id)
        Index 76: type2  list[list[str]] >> [['pizza_restaurant', 'Pizza'], ['fast_food_restaurant', 'Fast Food'], ['restaurant']]
        Index 78: google_place_id

        Index 82: address_split:list

        Index 84>0>0: popular_times

        Index 100: about (Serves brunch, Service options), tags
        Index 107: language
        Index 110: language_code
        Index 117: typical_time_spent


        Index 142: short_tags

        Index 153>0: reviews(tags) list
        Index 164>0>1: category
        Index 166: address_country_city:str

        Index 174: search_google_url

        Index 178: phones
        Index 178>0>0: phones text '+20 55 2366951'
        Index 178>0>1: list phones list[list[str, index]] with + and without +
        Index 178>0>3: phones '+20552366951'
        Index 178>0>5>0: phones 'tel:+20552366951'

        Index 183: address
        Index 183>1>0: district
        Index 183>1>1: street ???
        Index 183>1>2: street ???
        Index 183>1>3: city
        Index 183>1>4: postal_code ???
        Index 183>1>5: state
        Index 183>1>6: country_code
        Index 183>2>1>0: plus_code
        Index 203>0: working_hours, days
        """
        self.data = data

        self.rating: float = get_index(self.data, 4, 7, )
        self.reviews_count: int = get_index(self.data, 4, 8, )
        self.expensive_text: str = get_index(self.data, 4, 10, )

        self.site_url: str = get_index(self.data, 7, 0, )
        self.site_text: str = get_index(self.data, 7, 1, )

        self.latitude: float = get_index(self.data, 9, 2, )
        self.longitude: float = get_index(self.data, 9, 3, )
        self.google_id: str = get_index(self.data, 10, )
        self.hex_ids: str = get_index(self.data, 10, )

        self.title: str = get_index(self.data, 11, )
        self.type: str = get_index(self.data, 13, 0, )
        self.subtypes: list[str] = get_index(self.data, 13, default=[])
        self.full_address_name: str = get_index(self.data, 18, )
        self.time_zone: str = get_index(self.data, 30, )
        self.description: str = get_index(self.data, 32, 1, 1, )
        # TODO: Service
        # TODO: working_hours
        # TODO: images
        self.photos_count: int = get_index(self.data, 37, 1, )
        self.full_address: str = get_index(self.data, 39, )
        self.url: str = get_index(self.data, 42, )
        "https://www.google.com/maps/place/data=!4m6!3m5!1s0x14f7f1aaacd1b6ab:0x9537d45cb200e0ee!8m2!3d30.5889755!4d31.4919853!16s%2Fg%2F1tj70ytd?entry=ttu"
        # TODO: reviews_per_score
        # TODO: owner
        self.type2: list[list[str]] = get_index(self.data, 76, default=[])
        self.google_place_id: str = get_index(self.data, 78, )
        self.address_split: list = get_index(self.data, 82, default=[])
        # TODO: popular_times
        # TODO: about (Serves brunch, Service options), tags
        self.language: str = get_index(self.data, 110, )
        self.language_code: str = get_index(self.data, 117, )
        # TODO: typical_time_spent
        self.short_tags: list = get_index(self.data, 142, )
        # TODO: reviews(tags) list
        self.category: str = get_index(self.data, 164, 0, 1, )
        self.address_country_city: str = get_index(self.data, 166, )
        self.search_google_url: str = get_index(self.data, 174, )
        self.phone: str = get_index(self.data, 178, 0, 3, ) or get_index(self.data, 3, 0, )
        self.phone_format: str = get_index(self.data, 178, 0, 0)
        self.district: str = get_index(self.data, 183, 1, 0, )
        self.street: str = get_index(self.data, 183, 1, 1, )
        self.street_: str = get_index(self.data, 183, 1, 2, )
        self.city: str = get_index(self.data, 183, 1, 3, )
        self.postal_code: str = get_index(self.data, 183, 1, 4, )
        self.state: str = get_index(self.data, 183, 1, 5, )
        self.country_code: str = get_index(self.data, 183, 1, 6, )
        self.plus_code: str = get_index(self.data, 183, 2, 1, 0, )
        # TODO: working_hours, days

    def __repr__(self):
        return ('Place('
                f'title="{self.title}", '
                f'phone="{self.phone}", '
                f'category="{self.category}" ,'
                f'type="{self.type}" ,'
                f'rating="{self.rating}" ,'
                f'state="{self.state}" ,'
                f'city="{self.city}" ,'
                f'district="{self.district}" ,'
                f'street="{self.street}" ,'
                f'street_="{self.street_}" ,'
                ')')

    @property
    def name(self):
        return self.data[11]

    # @property
    # def phone(self):
    #     if self.data[178]:
    #         return self.data[178][0][3]
    #     elif self.data[3]:
    #         return self.data[3][0]

    @property
    def all_phones(self):
        if self.data[178]:
            return self.data[178]
        elif self.data[3]:
            return self.data[3]

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
    # def category(self) -> list:
    #     return self.data[13]

    # @property
    # def type2(self) -> list:
    #     return self.data[76]

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

    # @property
    # def short_tags(self):
    #     return self.data[142]

    @property
    # def language(self):
    #     return self.data[107]
    #
    # @property
    # def language_code(self):
    #     return self.data[110]

    # @property
    # def search_google_url(self):
    #     return self.data[174]

    # @property
    # def google_place_id(self):
    #     return self.data[78]

    @property
    def review_ids(self):
        return self.data[37][0][0][29]

    # @property
    # def hex_ids(self):
    #     return self.data[10]

    # @property
    # def url(self):
    #     return self.data[42]

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
            "days": self.days,
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
