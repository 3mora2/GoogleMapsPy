import json
from requests_html import HTMLSession
from fake_useragent import UserAgent
from GoogleMapspy.function import get_1d

ua = UserAgent()
session = HTMLSession()
word = "مطعم في الرياض"  # basically search words
# offset is the page number of the search result, the format is !8i+page,
# where page defaults to a multiple of 20, and when page is 0 (ie the first page), there is no !8i field in the url
offset = 0

p = 20
zoom = get_1d(0).get(9)  # !1d{3} is 1d, which is related to the zoom factor

longitude = "30.254350000000002"
latitude = "26.69425"
hl = "ar"  # the language, usually zh-CN or en or ar
gl = "eg"  # the abbreviation of the current country and region
url = (
    f"https://www.google.com/search?tbm=map&authuser=0&hl={hl}&gl={gl}&q={word}&oq={word}&"
    f"pb=!4m12!1m3!1d{zoom}!2d{longitude}!3d{latitude}!2m3!1f0!2f0!3f0!3m2!1i1536!2i686!4f13.1!7i{p}!8i{offset}"
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
# url = "https://www.google.com.hk/maps/place/{place}/@0,0,0z/data=!4m5!3m4!1s{longitude}!8m2!3d{latitude}!4d{location_code}"
# url = f"https://www.google.com.hk/maps/place/{word}/@0,0,0z"

headers = {
    "accept": "*/*",
    "referrer": "https://www.google.com/",
    "User-Agent": ua.random
}
r = session.request("GET", url, headers=headers)
# list_data = json.loads(r.text.replace(r"\n", "").replace(r"\/", "/")[4:])
list_data = json.loads(r.text[5:])
# list_data = json.loads(data.get("d"))
resturants = []
"11"
for ll in list_data[0][1][1:]:
    # restaurant = dict()
    # print(f"Name: {ll[14][11]}, Phone:{ll[14][178][0][3]} lat:{ll[14][9]}, Type:{ll[14][13]}")
    # restaurant['Name'] = ll[14][18].split(',', 1)[0]
    # restaurant['Address'] = ll[14][18].split(',', 1)[1] if "," in ll[14][18] else ll[14][18].split('،', 1)[1]
    # restaurant['Website'] = ll[14][7][1] if ll[14][7] else None
    # restaurant['Phone'] = ll[14][178][0][0]
    # restaurant['Rating'] = ll[14][4][7]
    # restaurant['Reviews'] = ll[14][4][8]
    # print(restaurant)
    # resturants.append(restaurant)

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
    print(va)