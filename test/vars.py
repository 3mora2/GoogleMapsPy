ll = []
va = {
    "split_unknown:str": ll[14][4][2],
    "split_reviews": {
        "reviews_url": ll[14][4][3][0],
        "reviews_count:str": ll[14][4][3][1],
        "reviews_count:int": ll[14][4][8]
    },
    "split_rate": ll[14][4][7],
    "split_website": {
        "url": ll[14][7][0] if ll[14][7] else None,
        "title": ll[14][7][1] if ll[14][7] else None,
    },
    "location": {
        "latitude": ll[14][9][2],
        "longitude": ll[14][9][3],
    },
    "name:str": ll[14][11],
    "type:list": ll[14][13],
    "type2:list": ll[14][76],
    "address": {
        "split_address:list": ll[14][2],
        "full": ll[14][18],
        "full_split:list": ll[14][183][0][0],
        "address": ll[14][39],
        "district": ll[14][14],
        "continent": ll[14][30],
        "address_split:list": ll[14][82],
        "address_country_city:str": ll[14][166],
        "all_address_list": ll[14][183]
    },
    "images": {
        "main": ll[14][37][0][0][6][0]
    },
    "tags:list": ll[14][100],
    "short_tags:list": ll[14][142],
    "lang": ll[14][107],
    "lang_code": ll[14][110],
    "search_google_url": ll[14][174],
    "phone:list": ll[14][178],
    "google_place_id": ll[14][78]

}

ll = []
var = {
                    "contrib_url": ll[0][0],
                    "contrib_name": ll[0][1],
                    "contrib_profile": ll[0][2],
                    "contrib_level": ll[12][0][0],
                    "contrib_reviews_count": ll[12][1][1],
                    "contrib_rate_count": ll[12][1][7],
                    "create_at": ll[1],
                    "review": ll[3],
                    "rate": ll[4],
                    "review_url": ll[18],
                    "lang": ll[32],
                    "place_name": ll[14][0][21][3][7][1],
                    "likes": ll[16],
                    "id": ll[61]
                }