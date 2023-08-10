from GoogleMapspy import GoogleMaps

maps = GoogleMaps(lang="en", country_code="eg")

# keyword = "مطعم في الرياض  و جدة"
# for index, place in enumerate(maps.search(keyword)):
#     print(index, place.name, place.phone)
#
# places = maps.search(keyword, streem=False, sleep_time=0)
# print(places)
place_name = "مطعم الكتكوت للمشويات، مدينة الروضة، مركز فارسكور"
place = maps.get_place(place_name)
print(place.name)
# ids = ["1511502518116541527", "2022987617800227988"]
# for i, v in enumerate(maps.get_reviews(*ids, sleep_time=1)):
#     print(i, v.json())
("https://www.google.com/maps/place/{name}/@{31.3279843},{31.7535306},{17}z/data="
 "!3m1!4b1!4m6!3m5!1s0x14f9e7860c2edadf:0xe7ee7daab22713f!8m2!3d{31.3279843}!4d{31.7535306}!16s%2Fg%2F11rn4ndyt8?authuser=0&hl=ar&entry=ttu")
"https://www.google.com/s?tbm=map&suggest=p&gs_ri=maps&psi=IJjUZMHEHtqskdUPifix-AE.1691654178763.1&gl=eg&hl=ar&authuser=0&q=%D9%85%D8%B7%D8%B9%D9%85+%D8%A7%D9%84%D9%83%D8%AA%D9%83%D9%88%D8%AA+%D9%84%D9%84%D9%85%D8%B4%D9%88%D9%8A%D8%A7%D8%AA%D8%8C+%D9%85%D8%AF%D9%8A%D9%86%D8%A9+%D8%A7%D9%84%D8%B1%D9%88%D8%B6%D8%A9%D8%8C+%D9%85%D8%B1%D9%83%D8%B2+%D9%81%D8%A7%D8%B1%D8%B3%D9%83%D9%88&ech=4&pb=!2i48!4m12!1m3!1d3044.2346010113743!2d31.75610552487107!3d31.327984274302622!2m3!1f0!2f0!3f0!3m2!1i1536!2i686!4f13.1!7i20!10b1!12m16!1m1!18b1!2m3!5m1!6e2!20e3!10b1!12b1!13b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m3!1sIJjUZMHEHtqskdUPifix-AE!7e81!17sIJjUZMHEHtqskdUPifix-AE%3A258!23m2!4b1!10b1!24m81!1m29!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m18!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!25b1!27m1!1b0!28b0!30b0!2b1!5m5!2b1!5b1!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!103b1!113b1!26m4!2m3!1i80!2i92!4i8!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!47m0!49m7!3b1!6m2!1b1!2b1!7m2!1e3!2b1!67m2!7b1!10b1!69i657"