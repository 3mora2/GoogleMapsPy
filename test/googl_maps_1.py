import json
# import os
#
# SOURCE_JSON_FILES = [
#     "sa_json/cities.json", "sa_json/districts.json", "sa_json/regions.json"]
#
# with open("sa_json/regions_lite.json", encoding="utf-8") as json_f:
#     json_regions = json.load(json_f)
#
# with open("sa_json/cities_lite.json", encoding="utf-8") as json_f:
#     json_cities = json.load(json_f)
#
# with open("sa_json/districts_lite.json", encoding="utf-8") as json_f:
#     json_districts = json.load(json_f)
#
# for district in json_districts:
#     city: dict = next(filter(lambda c: c["city_id"] == district["city_id"], json_cities))
#     if not city.get("districts"):
#         city["districts"] = []
#     city["districts"].append(district)
#
# for city in json_cities:
#     region: dict = next(filter(lambda c: c["region_id"] == city["region_id"], json_regions))
#     if not region.get("cities"):
#         region["cities"] = []
#     region["cities"].append(city)

# with open("sa_json/collect.json", "w", encoding="utf-8") as json_f:
#     json_f.write(str(json_regions))

# with open("sa_json/districts_lite_full.json", "w", encoding="utf-8") as json_f:
#     json_f.write(str(json_districts))

from GoogleMapspy import GoogleMaps

from sqlalchemy import create_engine, Column, String, JSON, Index, MetaData, INTEGER
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class GoogleMapsDB(Base):
    __tablename__ = 'kv_store'
    key = Column(INTEGER, primary_key=True)
    hex_ids = Column(String)
    data = Column(JSON)


class DB:
    def __init__(self):
        # Define the database path
        database_path = 'google_db_1.db'

        # Setup database and ORM
        engine = create_engine(f'sqlite:///{database_path}')
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()

    # def set(self, **kwargs):
    #     # value = json.dumps(value)
    #     # Query key-value pair
    #     # kv = self.session.query(KeyValue).filter_by(key=key).first()
    #     # if kv:
    #     #     kv.value = value
    #     # else:
    #     #     # Insert key-value pair
    #     kv = KeyValue(**kwargs)
    #     self.session.add(kv)
    #     self.session.commit()
    #     # return kv.value


db = DB()
old = []

# last = 0
if db.session.query(GoogleMapsDB).all():
    for q in db.session.query(GoogleMapsDB).all():
        old.append(q.hex_ids)
    # last = int(q.key)

maps = GoogleMaps(lang="ar", country_code="sa")
# url = "https://www.google.com/maps/place/%D8%A8%D9%8A%D8%AA%D8%B2%D8%A7+%D8%A5%D8%B3%D9%83%D9%86%D8%AF%D8%B1%D9%8A%D8%A9%E2%80%AD/@30.5890628,31.5035194,15.25z/data=!4m6!3m5!1s0x14f7f1aaacd1b6ab:0x9537d45cb200e0ee!8m2!3d30.5889755!4d31.4919853!16s%2Fg%2F1tj70ytd?entry=ttu"
# p = maps.get_place(url=url)
# print(p)


def scrap_text(text):
    # global last
    for index, place in enumerate(maps.search(text, add_oq=False, sleep_time=20), 1):
        if place.hex_ids in old:
            print("find")
            continue
        # last += 1
        old.append(place.hex_ids)
        print(len(old),  place)

        p = GoogleMapsDB(hex_ids=place.hex_ids, data=place.data)
        db.session.add(p)
    db.session.commit()


with open("sa_json/data.json", encoding="utf-8") as json_f:
    json_collect = json.load(json_f)

keyword = ["البقالات", "السوبر ماركت",
           "Grocery Store", "Supermarket", "shop", "store"]
for region in json_collect:
    for city in region["cities"]:
        if not city.get("districts"):
            for k in keyword:
                ke = f"{k} في {city["name_ar"]}"
                scrap_text(ke)
            continue

        for district in city["districts"]:
            for k in keyword:
                ke = f"{k} في {city["name_ar"]} {district["name_ar"]}"
                scrap_text(ke)

# maps = GoogleMaps(lang="en", country_code="sa")
# keyword = "restaurant في الرياض"
# for index, place in enumerate(maps.search(keyword, add_oq=False), 1):
#     print(index, place)
# url = "https://www.google.com/maps/place/%D8%A8%D9%8A%D8%AA%D8%B2%D8%A7+%D8%A5%D8%B3%D9%83%D9%86%D8%AF%D8%B1%D9%8A%D8%A9%E2%80%AD/@30.5890628,31.5035194,15.25z/data=!4m6!3m5!1s0x14f7f1aaacd1b6ab:0x9537d45cb200e0ee!8m2!3d30.5889755!4d31.4919853!16s%2Fg%2F1tj70ytd?entry=ttu"
# p = maps.get_place(url=url)
# print(p)
# [None, None, None, None, None, None, None, None, 's6OiZpr-Obrv4-EP06rMyAw', '0ahUKEwjao6Lz8sKHAxW69zgGHVMVE8kQmBkIAigA', ['مطعم', 0]]
# [None, None, None, None, None, None, None, None, 'EKSiZvqRA-Oa4-EPi8CvWA', '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQmBkIBCgB', None, None, None, None, ['EKSiZvqRA-Oa4-EPi8CvWA', '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQ8BcIBSgA', ['طريق العروبة', 'الورود', 'الرياض 12245'], None, [None, None, '$$$', ['https://search.google.com/local/reviews?placeid=ChIJdZEv6ecCLz4RgqQ02zKka6Y&q=%D9%85%D8%B7%D8%B9%D9%85+%D9%81%D9%8A+%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6&authuser=0&hl=ar&gl=SA', 'عدد التعليقات: ٧٬٣١١', None, '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQ6W4IFigB'], '$', None, None, 4.3, 7311, None, 'مكلف'], None, None, ['https://tokyoarabia.com/', 'tokyoarabia.com', None, None, ',AOvVaw3huyWGVDtxqYN87LWZ6-SX,,0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQ61gIFygP,'], None, [None, None, 24.7181459, 46.6867051], '0x3e2f02e7e92f9175:0xa66ba432db34a482', 'TOKYO - Al Wurud', None, ['مطعم مأكولات يابانية', 'مطعم راقٍ', 'مطعم المأكولات اليابانية الأصيلة', 'مطعم سوشي', 'مطعم وجبات تيبانياكي', 'مطعم شعيرية أودون'], 'الورود', None, None, None, 'TOKYO - Al Wurud، طريق العروبة، الورود، الرياض 12245', None, None, None, None, None, [[[[[2, None, None, None, None, [None, None, None, 0, 0], [None, None, None, 7, 0]], [2, None, None, None, None, [None, 30, 12], [None, 0, 24]]]]]], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [[[1], 'الأماكن المفضلة', None, 1, None, None, None, None, None, None, None, '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQwaQDCCUoAA'], [[2], 'أماكن أريد زيارتها', None, 1, None, None, None, None, None, None, None, '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQwaQDCCYoAQ'], [[7], 'خطط السفر', None, 1, None, None, None, None, None, None, None, '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQwaQDCCcoAg'], [[4], 'الأماكن المميّزة بنجمة', None, 1, None, None, None, None, None, None, None, '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQwaQDCCgoAw']], None, None, None, '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQ0JcGCCQoEw'], None, None, None, None, 'Asia/Riyadh', None, [[None, 'مأكولات يابانية متنوعة في محيط أنيق', None, None, None, 1], [None, 'مطعم راقٍ مختص في المأكولات اليابانية المبتكرة، بما فيها السوشي والتاكو والنودلز والحلويات', None, None, None, 1], None, 'https://www.google.com/local/review/rap/report?d=286732321&t=5&postId=0x3e2f02e7e92f9175:0xa66ba432db34a482%7C/g/11_r91tmr%7Car-SA', 'https://support.google.com/local-listings/answer/9851099'], None, [None, [['الخميس', ['١٢:٣٠م–١٢:٠٠ص'], None, None, '2024-07-25', 1, [[12, 30, 0, 0]], 0], ['الجمعة', ['١٢:٣٠م–١٢:٠٠ص'], None, None, '2024-07-26', 1, [[12, 30, 0, 0]], 0], ['السبت', ['١٢:٣٠م–١٢:٠٠ص'], None, None, '2024-07-27', 1, [[12, 30, 0, 0]], 0], ['الأحد', ['١٢:٣٠م–١٢:٠٠ص'], None, None, '2024-07-28', 1, [[12, 30, 0, 0]], 0], ['الاثنين', ['١٢:٣٠م–١٢:٠٠ص'], None, None, '2024-07-29', 1, [[12, 30, 0, 0]], 0], ['الثلاثاء', ['١٢:٣٠م–١٢:٠٠ص'], None, None, '2024-07-30', 1, [[12, 30, 0, 0]], 0], ['الأربعاء', ['١٢:٣٠م–١٢:٠٠ص'], None, None, '2024-07-31', 1, [[12, 30, 0, 0]], 0]], None, None, [['الخميس', ['١٢:٣٠م–١٢:٠٠ص'], None, None, '2024-07-25', 1, [[12, 30, 0, 0]], 0], 1, 1, 0, 'مفتوح ⋅ يغلق ١٢ ص'], None, ['الخميس', ['١٢:٣٠م–١٢:٠٠ص'], None, None, '2024-07-25', 1, [[12, 30, 0, 0]], 0], 2], None, None, [[['AF1QipMcT3rhXxumnfjQJl4Nn5CmyXFmSAsN2iCvyYg7', 10, 12, '', None, 858.962, ['https://lh5.googleusercontent.com/p/AF1QipMcT3rhXxumnfjQJl4Nn5CmyXFmSAsN2iCvyYg7=w122-h92-k-no', '6243 من الصور الإضافية', [4032, 3024], [80, 92]], None, [[3, 46.6865675, 24.7183979], [0, 90], [4032, 3024], 75], 'EKSiZvqRA-Oa4-EPi8CvWA', '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQzCcIKigA', None, None, None, None, [[['0x3e2f02e7e92f9175:0xa66ba432db34a482']]], None, ['طريق العروبة، الورود، الرياض 12245'], None, None, 'صورة', [None, [10, 'AF1QipMcT3rhXxumnfjQJl4Nn5CmyXFmSAsN2iCvyYg7'], [10, 3, [3024, 4032]], None, None, [[[2], [[None, None, 24.7183979, 46.6865675]]]], [2, None, None, [8], 2, [None, None, 'photos:gmm_android', [6, 7, 4, 1, 3]], None, None, [2018, 4, 4, 20]], None, None, None, None, None, None, None, None, None, None, None, None, ['UGCS_REFERENCE', 'CIHM0ogKEICAgIDkqvuu9QE||', '1']], 1, None, None, None, None, None, None, ['4480803349329842549', '-6454885102572493694'], None, 'K2GEdfm9T58']], 6243, None, 'EKSiZvqRA-Oa4-EPi8CvWA', None, 'EvgDKYQi49-NlUMIDwAAAAEAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGARCVCmEIuPfjZVD6AEAACAAAAADAAAABAAAAAQAAAAABAgAAAAAAAAAAAAEAQAAAACAAAQAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAEAIAAAAAAAAAAAA', None, None, [[[1, 187]], 1, None, 13, 187]], None, 'طريق العروبة، الورود، الرياض 12245', None, None, None, None, None, None, [['https://tokyoarabia.com/#reser', 'tokyoarabia.com', None, None, ',AOvVaw3huyWGVDtxqYN87LWZ6-SX,,0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQ2ZABCCIoEQ,'], ['https://www.sevenrooms.com/reservations/tokyoalorubaroad/ig?instant_experiences_enabled=true&venues=tokyoalghadir%2Ctokyoalorubaroad&fbclid=PAAabMLHHK5xhcVNcA10_cdfNtudcMkQ6Sk2whACjcFLwZZ9WicpYoezlBkqc_aem_AWGOST4878Y0ls4v6wURaIZL3QDns9Swqt65AMlV-eU9iYbvOY&fbclid=PAAaYy9PjxGKDfg8SfDiX9Ucz35FVwV34Gh3Yy9QrWc38WUkHzwgpTruXDKus_aem_AfSqY_04kVK30NPyhaIyPy9Zp0pFcrEleNFd1ulqiT4iQ2qrCQctD38cPCeWKWnN3iA', 'sevenrooms.com', None, None, ',AOvVaw2WB5hd9SZyRq7ZQUXh7KZ3,,0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQ2ZABCCMoEg,']], None, None, None, None, None, [None, None, None, [383, 220, 572, 1434, 4702], None, None, None, None, None, ['التقييم والمراجعة', 'شارِك تجربتك لمساعدة الآخرين', None, 1, 'يُرجى مشاركة تفاصيل تجربتك في هذا المكان'], None, None, None, None, None, 0], None, None, None, None, [None, 'TOKYO - Al Wurud (المالك)', '112702151383465108059', None, None, None, None, None, '112702151383465108059'], None, None, None, 1, None, None, None, None, None, 1, None, None, None, None, [[['AF1QipMcT3rhXxumnfjQJl4Nn5CmyXFmSAsN2iCvyYg7', 10, 12, '', None, 858.962, ['https://lh5.googleusercontent.com/p/AF1QipMcT3rhXxumnfjQJl4Nn5CmyXFmSAsN2iCvyYg7=w114-h86-k-no', 'TOKYO - Al Wurud', [4032, 3024], [86, 86]], None, [[3, 46.6865675, 24.7183979], [0, 90], [4032, 3024], 75], 'EKSiZvqRA-Oa4-EPi8CvWA', '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQzCcIKygV', None, None, None, None, [[['0x3e2f02e7e92f9175:0xa66ba432db34a482']]], None, ['طريق العروبة، الورود، الرياض 12245'], None, None, 'صورة', [None, [10, 'AF1QipMcT3rhXxumnfjQJl4Nn5CmyXFmSAsN2iCvyYg7'], [10, 3, [3024, 4032]], None, None, [[[2], [[None, None, 24.7183979, 46.6865675]]]], [2, None, None, [8], 2, [None, None, 'photos:gmm_android', [6, 7, 4, 1, 3]], None, None, [2018, 4, 4, 20]], None, None, None, None, None, None, None, None, None, None, None, None, ['UGCS_REFERENCE', 'CIHM0ogKEICAgIDkqvuu9QE||', '1']], 1, None, None, None, None, None, None, ['4480803349329842549', '-6454885102572493694'], None, 'K2GEdfm9T58'], ['AF1QipMcT3rhXxumnfjQJl4Nn5CmyXFmSAsN2iCvyYg7', 10, 12, '', None, 858.962, ['https://lh5.googleusercontent.com/p/AF1QipMcT3rhXxumnfjQJl4Nn5CmyXFmSAsN2iCvyYg7=w408-h306-k-no', 'TOKYO - Al Wurud', [4032, 3024], [408, 240]], None, [[3, 46.6865675, 24.7183979], [0, 90], [4032, 3024], 75], 'EKSiZvqRA-Oa4-EPi8CvWA', '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQzCcILCgW', None, None, None, None, [[['0x3e2f02e7e92f9175:0xa66ba432db34a482']]], None, ['طريق العروبة، الورود، الرياض 12245'], None, None, 'صورة', [None, [10, 'AF1QipMcT3rhXxumnfjQJl4Nn5CmyXFmSAsN2iCvyYg7'], [10, 3, [3024, 4032]], None, None, [[[2], [[None, None, 24.7183979, 46.6865675]]]], [2, None, None, [8], 2, [None, None, 'photos:gmm_android', [6, 7, 4, 1, 3]], None, None, [2018, 4, 4, 20]], None, None, None, None, None, None, None, None, None, None, None, None, ['UGCS_REFERENCE', 'CIHM0ogKEICAgIDkqvuu9QE||', '1']], 1, None, None, None, None, None, None, ['4480803349329842549', '-6454885102572493694'], None, 'K2GEdfm9T58']]], None, None, [[[1, None, [[['tokyoarabia.com'], [None, None, ['https://tokyoarabia.com/#reser', ['https://tokyoarabia.com/#reser', None, None, None, ',AOvVaw3huyWGVDtxqYN87LWZ6-SX,,0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQtxwILygA,']]], 1], [['sevenrooms.com'], [None, None, ['https://www.sevenrooms.com/reservations/tokyoalorubaroad/ig?instant_experiences_enabled=true&venues=tokyoalghadir%2Ctokyoalorubaroad&fbclid=PAAabMLHHK5xhcVNcA10_cdfNtudcMkQ6Sk2whACjcFLwZZ9WicpYoezlBkqc_aem_AWGOST4878Y0ls4v6wURaIZL3QDns9Swqt65AMlV-eU9iYbvOY&fbclid=PAAaYy9PjxGKDfg8SfDiX9Ucz35FVwV34Gh3Yy9QrWc38WUkHzwgpTruXDKus_aem_AfSqY_04kVK30NPyhaIyPy9Zp0pFcrEleNFd1ulqiT4iQ2qrCQctD38cPCeWKWnN3iA', ['https://www.sevenrooms.com/reservations/tokyoalorubaroad/ig?instant_experiences_enabled=true&venues=tokyoalghadir%2Ctokyoalorubaroad&fbclid=PAAabMLHHK5xhcVNcA10_cdfNtudcMkQ6Sk2whACjcFLwZZ9WicpYoezlBkqc_aem_AWGOST4878Y0ls4v6wURaIZL3QDns9Swqt65AMlV-eU9iYbvOY&fbclid=PAAaYy9PjxGKDfg8SfDiX9Ucz35FVwV34Gh3Yy9QrWc38WUkHzwgpTruXDKus_aem_AfSqY_04kVK30NPyhaIyPy9Zp0pFcrEleNFd1ulqiT4iQ2qrCQctD38cPCeWKWnN3iA', None, None, None, ',AOvVaw2WB5hd9SZyRq7ZQUXh7KZ3,,0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQtxwIMCgB,']]]]], None, 21631]]], [['japanese_restaurant', 'الياباني'], ['fine_dining_restaurant', 'مطاعم فاخرة'], ['japanese_authentic_restaurant', 'مأكولات يابانية أصيلة'], ['sushi_restaurant', 'سوشي'], ['teppan_grill_restaurant', 'تيبانياكي'], ['udon_noodle_shop', 'معكرونة أودون']], None, 'ChIJdZEv6ecCLz4RgqQ02zKka6Y', None, None, None, ['الورود', 'طريق العروبة', 'طريق العروبة', 'الرياض'], None, None, None, None, None, ['مأكولات يابانية متنوعة في محيط أنيق', 'SearchResult.TYPE_JAPANESE_RESTAURANT', ['SearchResult.TYPE_JAPANESE_RESTAURANT', 'SA', 32, 84, 85, 151], 'TOKYO - Al Wurud', [None, None, 188, 187, 1166, 186]], '/g/11_r91tmr', None, None, None, None, None, None, None, None, None, None, [[['/geo/type/establishment_poi/serves_brunch', 'إفطار متأخر', [1, [[1, 'إفطار متأخر']], [1, 'إفطار متأخر', 'إفطار متأخر', 'تقديم وجبات الإفطار المتأخر']], None, [1], 0]], [['service_options', 'خيارات الخدمة', [['/geo/type/establishment/has_no_contact_delivery', 'التسليم بدون تلامس', [1, [[1, 'التسليم بدون تلامس']], [1, 'التسليم بدون تلامس', 'التسليم بدون تلامس', 'يتوفّر التسليم بدون تلامس']], None, [34], 0], ['/geo/type/establishment_poi/has_delivery', 'خدمة التوصيل', [1, [[1, 'خدمة التوصيل']], [1, 'خدمة التوصيل', 'خدمة التوصيل', 'خدمة التوصيل للمنازل']], None, [1], 0], ['/geo/type/establishment_poi/has_takeout', 'طعام سفري', [1, [[1, 'طعام سفري']], [1, 'طعام سفري', 'طعام سفري', 'يوفّر طعام سفري']], None, [1], 0], ['/geo/type/establishment_poi/serves_dine_in', 'الجلوس داخل المكان', [1, [[1, 'الجلوس داخل المكان']], [1, 'الجلوس داخل المكان', 'الجلوس داخل المكان', 'يوفّر خدمة الأكل داخل المكان']], None, [1], 0]]], ['highlights', 'أهم السمات', [['/geo/type/establishment_poi/has_fast_service', 'خدمة سريعة', [1, [[1, 'خدمة سريعة']], [1, 'خدمة سريعة', 'خدمة سريعة', 'توجد خدمة سريعة']], None, [1], 0]]], ['accessibility', 'إمكانية الوصول', [['/geo/type/establishment_poi/has_wheelchair_accessible_seating', 'أماكن جلوس صالحة للكراسي المتحركة', [1, [[1, 'أماكن جلوس صالحة للكراسي المتحركة']], [1, 'أماكن جلوس صالحة للكراسي المتحركة', 'أماكن جلوس صالحة للكراسي المتحركة', 'تتوفَّر أماكن جلوس صالحة للكراسي المتحركة']], None, [1], 0], ['/geo/type/establishment_poi/has_wheelchair_accessible_restroom', 'دورة مياه تستوعب الكراسي المتحركة', [1, [[1, 'دورة مياه تستوعب الكراسي المتحركة']], [1, 'دورة مياه تستوعب الكراسي المتحركة', 'دورة مياه تستوعب الكراسي المتحركة', 'به دورة مياه تستوعب الكراسي المتحركة']], None, [1], 0], ['/geo/type/establishment_poi/has_wheelchair_accessible_entrance', 'مدخل صالح للكراسي المتحركة', [1, [[1, 'مدخل صالح للكراسي المتحركة']], [1, 'مدخل صالح للكراسي المتحركة', 'مدخل صالح للكراسي المتحركة', 'يتوفَّر مدخل صالح للكراسي المتحركة']], None, [1], 0], ['/geo/type/establishment_poi/has_wheelchair_accessible_parking', 'موقف سيارات صالح للكراسي المتحركة', [1, [[1, 'موقف سيارات صالح للكراسي المتحركة']], [1, 'موقف سيارات صالح للكراسي المتحركة', 'موقف سيارات صالح للكراسي المتحركة', 'يتوفَّر موقف سيارات صالح للكراسي المتحركة']], None, [1], 0]]], ['offerings', 'الخدمات المقدّمة', [['/geo/type/establishment_poi/serves_organic', 'المأكولات العضوية', [1, [[1, 'المأكولات العضوية']], [1, 'المأكولات العضوية', 'المأكولات العضوية', 'يقدم المأكولات العضوية']], None, [1], 0], ['/geo/type/establishment/serves_vegan', 'خيارات خالية من المنتجات الحيوانية', [1, [[1, 'خيارات خالية من المنتجات الحيوانية']], [1, 'خيارات خالية من المنتجات الحيوانية', 'خيارات خالية من المنتجات الحيوانية', 'يقدّم أطباقًا خالية من المشتقات الحيوانية']], None, [1], 0], ['/geo/type/establishment_poi/serves_healthy', 'خيارات صحية', [1, [[1, 'خيارات صحية']], [1, 'خيارات صحية', 'خيارات صحية', 'تقديم خيارات أطعمة صحية']], None, [1], 0], ['/geo/type/establishment_poi/serves_vegetarian', 'خيارات نباتية', [1, [[1, 'خيارات نباتية']], [1, 'خيارات نباتية', 'خيارات نباتية', 'يقدّم أطباقًا نباتية']], None, [1], 0], ['/geo/type/establishment_poi/serves_coffee', 'قهوة', [1, [[1, 'قهوة']], [1, 'قهوة', 'قهوة', 'تقديم القهوة']], None, [1], 0], ['/geo/type/establishment_poi/serves_late_night_food', 'مأكولات في ساعات متأخرة من الليل', [1, [[1, 'مأكولات في ساعات متأخرة من الليل']], [1, 'مأكولات في ساعات متأخرة من الليل', 'مأكولات في ساعات متأخرة من الليل', 'يقدم مأكولات في ساعات متأخرة من الليل']], None, [1], 0], ['/geo/type/establishment_poi/quick_bite', 'مطعم وجبات سريعة', [1, [[1, 'مطعم وجبات سريعة']], [1, 'مطعم وجبات سريعة', 'مطعم وجبات سريعة', 'وجبات سريعة']], None, [1], 0], ['/geo/type/establishment_poi/serves_small_plates', 'وجبات خفيفة', [1, [[1, 'وجبات خفيفة']], [1, 'وجبات خفيفة', 'وجبات خفيفة', 'يقدم وجبات خفيفة']], None, [1], 0]]], ['dining_options', 'خيارات تناول الطعام', [['/geo/type/establishment_poi/serves_brunch', 'إفطار متأخر', [1, [[1, 'إفطار متأخر']], [1, 'إفطار متأخر', 'إفطار متأخر', 'تقديم وجبات الإفطار المتأخر']], None, [1], 0], ['/geo/type/establishment_poi/serves_lunch', 'الغداء', [1, [[1, 'الغداء']], [1, 'الغداء', 'الغداء', 'تقديم وجبات الغداء']], None, [1], 0], ['/geo/type/establishment_poi/serves_dinner', 'العشاء', [1, [[1, 'العشاء']], [1, 'العشاء', 'العشاء', 'تقديم وجبات العشاء']], None, [1], 0], ['/geo/type/establishment_poi/has_catering', 'خدمات التزويد بالطعام', [1, [[1, 'خدمات التزويد بالطعام']], [1, 'خدمات التزويد بالطعام', 'خدمات التزويد بالطعام', 'يوجد تقديم أطعمة']], None, [1], 0], ['/geo/type/establishment_poi/serves_dessert', 'الحلويات', [1, [[1, 'الحلويات']], [1, 'الحلويات', 'الحلويات', 'يقدم حلويات']], None, [1], 0], ['/geo/type/establishment_poi/has_seating', 'أماكن الجلوس', [1, [[1, 'أماكن الجلوس']], [1, 'أماكن الجلوس', 'أماكن الجلوس', 'توجد أماكن جلوس']], None, [1], 0]]], ['amenities', 'وسائل الراحة', [['/geo/type/establishment_poi/has_restroom', 'دورة مياه', [1, [[1, 'دورة مياه']], [1, 'دورة مياه', 'دورة مياه', 'توجد دورة مياه']], None, [1], 0]]], ['atmosphere', 'الأجواء', [['/geo/type/establishment_poi/feels_casual', 'غير رسمي', [1, [[1, 'غير رسمي']], [1, 'غير رسمي', 'غير رسمي', 'غير رسمي']], None, [1], 0], ['/geo/type/establishment_poi/feels_cozy', 'مريح', [1, [[1, 'مريح']], [1, 'مريح', 'مريح', 'مريح']], None, [1], 0]]], ['crowd', 'الجمهور', [['/geo/type/establishment_poi/suitable_for_groups', 'مجموعات', [1, [[1, 'مناسب للمجموعات']], [1, 'مناسب للمجموعات', 'مجموعات', 'مناسب للمجموعات']], None, [1], 0]]], ['planning', 'التخطيط', [['/geo/type/establishment_poi/accepts_reservations', 'يقبل الحجوزات', [1, [[1, 'يقبل الحجوزات']], [1, 'يقبل الحجوزات', 'يقبل الحجوزات', 'يقبل الحجوزات']], None, [1], 0]]], ['payments', 'الدفعات', [['/geo/type/establishment_poi/pay_credit_card', 'بطاقات الائتمان', [1, [[1, 'بطاقات الائتمان']], [1, 'بطاقات الائتمان', 'بطاقات الائتمان', 'يتم قبول بطاقات الائتمان']], None, [1], 0], ['/geo/type/establishment_poi/pay_debit_card', 'بطاقات السحب الآلي', [1, [[1, 'بطاقات السحب الآلي']], [1, 'بطاقات السحب الآلي', 'بطاقات السحب الآلي', 'يتم قبول بطاقات السحب الآلي']], None, [1], 0], ['/geo/type/establishment_poi/pay_mobile_nfc', 'دفعات أجهزة الجوّال عبر NFC', [1, [[1, 'دفعات أجهزة الجوّال عبر NFC']], [1, 'دفعات أجهزة الجوّال عبر NFC', 'دفعات أجهزة الجوّال عبر NFC', 'يتم قبول دفعات أجهزة الجوّال عبر NFC']], None, [1], 0]]], ['children', 'أطفال', [['/geo/type/establishment_poi/has_high_chairs', 'الكراسي العالية', [1, [[1, 'الكراسي العالية']], [1, 'الكراسي العالية', 'الكراسي العالية', 'تتوفر كراسٍ عالية']], None, [1], 0], ['/geo/type/establishment_poi/welcomes_children', 'مناسب للأطفال', [1, [[1, 'مناسب للأطفال']], [1, 'مناسب للأطفال', 'مناسب للأطفال', 'مناسب للأطفال']], None, [9], 0]]], ['parking', 'موقف سيارات', [['/geo/type/establishment_poi/parking_availability', 'موقف سيارات', [2, None, None, ['/g/11kjq52z3w', 1, 'تتوفّر مواقف كثيرة للسيارات', 'تتوفّر مواقف كثيرة للسيارات']], None, [1], 0], ['/geo/type/establishment_poi/has_parking_lot_free', 'موقف سيارات مجاني', [1, [[1, 'موقف سيارات مجاني']], [1, 'موقف سيارات مجاني', 'موقف سيارات مجاني', 'موقف سيارات مجاني']], None, [1], 0], ['/geo/type/establishment_poi/has_parking_street_free', 'موقف سيارات مجاني في الشارع', [1, [[1, 'موقف سيارات مجاني في الشارع']], [1, 'موقف سيارات مجاني في الشارع', 'موقف سيارات مجاني في الشارع', 'موقف سيارات مجاني في الشارع']], None, [1], 0]]]], None, [['/geo/type/establishment_poi/serves_dine_in', 'الجلوس داخل المكان', [1, [[1, 'الجلوس داخل المكان']], [1, 'الجلوس داخل المكان', 'الجلوس داخل المكان', 'يوفّر خدمة الأكل داخل المكان']], None, [1], 0], ['/geo/type/establishment_poi/has_takeout', 'طعام سفري', [1, [[1, 'طعام سفري']], [1, 'طعام سفري', 'طعام سفري', 'يوفّر طعام سفري']], None, [1], 0], ['/geo/type/establishment/has_no_contact_delivery', 'التسليم بدون تلامس', [1, [[1, 'التسليم بدون تلامس']], [1, 'التسليم بدون تلامس', 'التسليم بدون تلامس', 'يتوفّر التسليم بدون تلامس']], None, [34], 0]]], None, None, None, None, None, None, None, None, None, 'ar', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, [None, [[None, None, None, 95071, None, None, [[[['الجلوس داخل المكان'], None, None, None, 'الجلوس داخل المكان'], [['طعام سفري'], None, None, None, 'طعام سفري'], [['التسليم بدون تلامس'], None, None, None, 'التسليم بدون تلامس']]], None, None, None, None, None, '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQ7MIHCDEoGQ']]], None, None, None, [9], None, None, None, [None, None, 1], None, None, None, None, None, None, 'https://lh4.googleusercontent.com/-5P-uQH8w9P4/AAAAAAAAAAI/AAAAAAAAAAA/X23iCIOGoa4/s44-p-k-no-ns-nd/photo.jpg', None, None, None, None, None, None, [[8, 'المطاعم'], 'عرض المطاعم القريبة'], [1], 'الرياض', None, None, None, None, None, None, None, ['https://www.google.com/search?q=local+guide+program&ibp=gwp;0,26,OiMKISIdVE9LWU8gLSBBbCBXdXJ1ZCDYp9mE2LHZitin2LYoAg&pcl=lp'], None, None, None, [['9200 09662', [['9200 09662', 1], ['+966 9200 09662', 2]], None, '920009662', None, ['tel:920009662', None, None, '0ahUKEwj62Zef88KHAxVjzTgGHQvgCwsQ_doBCBMoDQ']]], None, None, [None, None, None, None, None, '15006709069034980392', '112702151383465108059'], None, [[[7, [['TOKYO - Al Wurud'], ['طريق العروبة'], ['الورود'], ['الرياض 12245']]], [2, [['TOKYO - Al Wurud، طريق العروبة، الورود، الرياض 12245']]], [1, [['طريق العروبة، الورود، الرياض 12245']]], [4, [['الرياض']]]], ['الورود', 'طريق العروبة', 'طريق العروبة', 'الرياض', None, None, 'SA']], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [[['الخميس', 4, [2024, 7, 25], [['١٢:٣٠م–١٢:٠٠ص', [[12, 30], []]]], 0, 1], ['الجمعة', 5, [2024, 7, 26], [['١٢:٣٠م–١٢:٠٠ص', [[12, 30], []]]], 0, 1], ['السبت', 6, [2024, 7, 27], [['١٢:٣٠م–١٢:٠٠ص', [[12, 30], []]]], 0, 1], ['الأحد', 7, [2024, 7, 28], [['١٢:٣٠م–١٢:٠٠ص', [[12, 30], []]]], 0, 1], ['الاثنين', 1, [2024, 7, 29], [['١٢:٣٠م–١٢:٠٠ص', [[12, 30], []]]], 0, 1], ['الثلاثاء', 2, [2024, 7, 30], [['١٢:٣٠م–١٢:٠٠ص', [[12, 30], []]]], 0, 1], ['الأربعاء', 3, [2024, 7, 31], [['١٢:٣٠م–١٢:٠٠ص', [[12, 30], []]]], 0, 1]], [['الخميس', 4, [2024, 7, 25], [['١٢:٣٠م–١٢:٠٠ص', [[12, 30], []]]], 0, 1], 0, 1, None, ['مفتوح ⋅ يغلق ١٢ ص', [[0, 5, [None, [4279795768, 4286695829]]]]], ['مفتوح ⋅ يغلق ١٢ ص', [[0, 5, [None, [4279795768, 4286695829]]]]], None, None, ['مفتوح', [[0, 5, [None, [4279795768, 4286695829]]]]]], 4, 2, None, None, 6], None, 1, None, None, [[None, None, 24.7181459, 46.6867051]], 'ChrZhdi32LnZhSDZgdmKINin2YTYsdmK2KfYtlocIhrZhdi32LnZhSDZgdmKINin2YTYsdmK2KfYtpIBE2phcGFuZXNlX3Jlc3RhdXJhbnSaASRDaGREU1VoTk1HOW5TMFZKUTBGblNVTkhhM1ZJVm5ablJSQULgAQA', None, None, None, None, 1, None, None, None, None, None, None, None, None, None, None, None, None, [['0x3e2f02e7e92f9175:0xa66ba432db34a482', None, None, '/g/11_r91tmr', 'ChIJdZEv6ecCLz4RgqQ02zKka6Y', '15006709069034980392', '112702151383465108059']], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'SA']]
