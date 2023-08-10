# New


The parameters are structured like (`![id][type][value]`), with types:
```
m: matrix
f: float
d: double
i: integer
b: boolean
e: enum (as integer)
s: string
u: unsigned int


d - double precision floating point
f - single precision floating point
i - integer
s - string
z - encoded data or an id or some kind
b - byte or boolean (?)
e - (?)
v - timestamp, unix epoch in milliseconds
```

Matrices can encapsulate multiple data entries, e.g. `!1m3!1i2!1i4!1i17` means that the `matrix`(`m`) with the ID `1` contains the three integer values [2, 4, 17].

# https://serpapi.com/maps-local-results
# https://github.com/iewoai/GoogleMap_Spider/blob/master/main.py
# https://medium.com/@supun1001/how-to-generate-google-embed-links-programmatically-for-iframes-for-routes-only-d6dc225e59e8
# https://andrewwhitby.com/2014/09/09/google-maps-new-embed-format/