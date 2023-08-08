## This Readme translated from [GoogleMap_Spider](https://github.com/iewoai/GoogleMap_Spider/blob/master/main.py) explain  google search map url

[iewoai] Crawl the business information of Google Maps (requests version)

# Google map crawler (requests version)
## 1. Goal: Search company, change coordinates, get all company information on Google Maps
#### Note: The requests version simply implements the crawling logic, and does not take into account other aspects, such as duplicate checking, crawling speed, etc.
## Idea: Starting from a point, select the optimal Z of the point (adjusted by an integer), use the slice side length of the point or 1d expression as the distance, and the movement difference of the longitude and latitude is equal, and repeat this step for each point after the movement.
### The following is purely personal understanding:
### 1. The same latitude and longitude, the number of companies with different zoom factors is not the same, it is difficult to choose the optimal value
### 2. When there is no optimal value, that is, there is no company near the coordinate, you need to set the default range (latitude and longitude increase and decrease range)
### 3. When moving, move forward, backward, left, and right, that is, fix the longitude or latitude, and move the other positive and negative
### 4. Fixed latitude and dynamic longitude, degree difference is affected by latitude and distance; fixed longitude and dynamic latitude, degree difference is only affected by distance
### 5. The optimal value is the multiple with the largest number of companies in the company with a zoom factor greater than or equal to 12 (latitude range 0.82739) and less than or equal to 18 (latitude range 0.00899). Use its 1d (see url analysis) as the distance, up, down, left, and right move. When the number of 12-18 companies is 0, take the default range


## 2. Tile map principle reference materials:
### 1. https://segmentfault.com/a/1190000011276788
### 2. https://blog.csdn.net/mygisforum/article/details/8162751
### 3. https://www.maptiler.com/google-maps-coordinates-tile-bounds-projection/
### 4. https://blog.csdn.net/mygisforum/article/details/13295223


## Three, url analysis 1
#### Example: url = 'https://www.google.com/maps/search/company/@43.8650268,-124.6372106,3.79z'
#### https://www.google.com/maps/search/company/@X,Y,Z
### 1. X latitude, range [-85.05112877980659, 85.05112877980659]
### 2. Y longitude, range [-180, 180]
### 3. Z zoom factor, range [2, 21]
### 4. Z=2 slice square side length is 20037508.3427892
## url parsing 2
#### Example: https://www.google.com/search?tbm=map&authuser=0&hl={1}&gl={2}&pb=!4m9!1m3!1d{3}!2d{4}!3d{5}!2m0!3m2!1i784!2i644!4f13.1!7i20{6}!10b1!12m8!1m1!18b1!2m3!5m1!6e2!20e3!10b1!16b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1sg3qzXsG-JpeGoATHyYKQBw%3A1!2zMWk6MSx0OjExODg3LGU6MCxwOmczcXpYc0ctSnBlR29BVEh5WUtRQnc6MQ!7e81!12e3!17sg3qzXsG-JpeGoATHyYKQBw%3A110!18e15!24m46!1m12!13m6!2b1!3b1!4b1!6i1!8b1!9b1!18m4!3b1!4b1!5b1!6b1!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!30m1!2b1!36b1!43b1!52b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i644!1m6!1m2!1i734!2i0!2m2!1i784!2i644!1m6!1m2!1i0!2i0!2m2!1i784!2i20!1m6!1m2!1i0!2i624!2m2!1i784!2i644!34m13!2b1!3b1!4b1!6b1!8m3!1b1!3b1!4b1!9b1!12b1!14b1!20b1!23b1!37m1!1e81!42b1!47m0!49m1!3b1!50m4!2e2!3m2!1b1!3b0!65m0&q={7}&oq={8}&gs_l=maps.12...0.0.1.12357296.1.1.0.0.0.0.0.0..0.0....0...1ac..64.maps..1.0.0.0...3041.&tch=1&ech=1&psi=g3qzXsG-JpeGoATHyYKQBw.1588820611303.1
### 1. hl={1} is the language, usually zh-CN or en
### 2. g1={2} is the abbreviation of the current country and region
### 3. !1d{3} is 1d, which is related to the zoom factor. The relationship between two adjacent integer zoom factors is 1/2. The higher the zoom factor, the smaller the value. The maximum is 94618532.08008283, which is the current map. Slice side length or perimeter equilateral proportional relationship
### 4. !2d{4} is 2d, longitude
### 5. !3d{5} is 3d, latitude
### 6. {6} is the page number of the search result, the format is !8i+page, where page defaults to a multiple of 20, and when page is 0 (ie the first page), there is no !8i field in the url
### 7. q={7}&oq={8}, basically search words


## 4. Interchange between latitude and longitude and distance
### 1. Source: https://blog.csdn.net/qq_37742059/article/details/101554565