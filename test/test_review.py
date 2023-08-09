import json
from requests_html import HTMLSession
from fake_useragent import UserAgent

ua = UserAgent()
session = HTMLSession()

hl = "ar"  # the language, usually zh-CN or en or ar
gl = "eg"  # the abbreviation of the current country and region
page = 10
url = (
    f"https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl={hl}&gl={gl}&"
    f"pb=!1m2!1y{1511502518116541527}!2y{2022987617800227988}!2m1!2i{page}!3e1!4m5!3b1!4b1!6b1!7b1!20b1!5m2!1sJavSZPiQCfGqkdUPx469kA4!7e81")

headers = {
    "accept": "*/*",
    "referrer": "https://www.google.com/",
    "User-Agent": ua.random
}
r = session.request("GET", url, headers=headers)
# list_data = json.loads(r.text.replace(r"\n", "").replace(r"\/", "/")[4:])
list_data = json.loads(r.text[5:])
# list_data = json.loads(data.get("d"))

for ll in list_data[2]:
    var = {
        "contrib_url": ll[0][0],
        "contrib_name": ll[0][1],
        "contrib_profile": ll[0][2],
        "contrib_level": ll[12][0][0] if ll[12][0] else None,
        "contrib_reviews_count": ll[12][1][1],
        "contrib_rate_count": ll[12][1][7],
        "create_at": ll[1],
        "review": ll[3],
        "rate": ll[4],
        "review_url": ll[18],
        "lang": ll[32],
        "place_name": ll[14][0][21][3][7][1] if ll[14] else None,
        "likes": ll[16],
        "id":ll[61]
    }
