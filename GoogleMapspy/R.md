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

case matrix = "m"
case enumerator = "e"
case string = "s"
case base64 = "z"
case double = "d"
case float = "f"
case timestamp = "v"
case integer = "i"
case unknown = "u"

pattern = "(\\d+)([a-zA-Z]{1})(.+)"

case panoramaId = "3.3.1"
case userContent = "3.3.6"
case userContentWidth = "3.3.7"
case userContentHeight = "3.3.8"
case latitude = "4.3.8.3"
case longitude = "4.3.8.4"
```


```

"https://www.google.com/maps/preview/place?authuser=0&hl=en&gl=uk&pb=!1m18!1s0x883889c1b990de71"
"%3A0xe43266f8cfb1b533!3m12!1m3!1d927320.1486093864!2d-83.54278581348586!3d40.20785822959047!2m3!1f0!2f0"
"!3f0!3m2!1i1280!2i913!4f13.1!4m2!3d39.961332959837826!4d-82.99896240234375!5e1!12m4!2m3!1i360!2i120!4i8"
"!13m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2"
"!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3"
"!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!14m5!1sbAKXZMrfGPqA9u8Pn7KG4AE!4m1!2i9853!7e81!12e3!15m82!1m30"
"!4e2!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m18!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1"
"!21b1!22b0!25b1!27m1!1b0!28b0!30b0!2b1!5m5!2b1!5b1!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3"
"!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3"
"!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!103b1!113b1!21m28!1m6!1m2!1i0!2i0!2m2!1i530!2i913!1m6!1m2"
"!1i1230!2i0!2m2!1i1280!2i913!1m6!1m2!1i0!2i0!2m2!1i1280!2i20!1m6!1m2!1i0!2i893!2m2!1i1280!2i913!22m2!1e81"
"!8e1!29m0!30m3!3b1!6m1!2b1!34m2!7b1!10b1!37i652!39sColumbus&q=Columbus"
------------------
1m:
!1s: date (filter), data_id
!9i: price (filter)
3m:
1m:
1d:
2d:
3d:
1s0x0%3A0x1c13188527ff0c94
0x1c13188527ff0c94 -> 2022987617800227988
ast.literal_eval("0x1c13188527ff0c94")
https://google.com/maps?cid=2022987617800227988
%3A -> :
1s0x0:0x1c13188527ff0c94 -> 0x0 -> 0 : 0x1c13188527ff0c94 -> 2022987617800227988
1s = 0:2022987617800227988

-----
!1stRLSZM7lG--0kdUPh8SyiAM%3A4
!1stRLSZM7lG--0kdUPh8SyiAM:4
tRLSZM7lG--0kdUPh8SyiAM:4
------
!2s1i%3A0%2Ct%3A11886%2Cp%3AtRLSZM7lG--0kdUPh8SyiAM%3A4
!2s1i:0%2Ct:11886%2Cp:tRLSZM7lG--0kdUPh8SyiAM:4
1i:0,t:11886,p:tRLSZM7lG--0kdUPh8SyiAM:4
1i: 0
t: 11886
p: tRLSZM7lG--0kdUPh8SyiAM:4
p -> refare to !1s

```
Matrices can encapsulate multiple data entries, e.g. `!1m3!1i2!1i4!1i17` means that the `matrix`(`m`) with the ID `1` contains the three integer values [2, 4, 17].

https://github.com/dvoeglazov-dev/GoogleUrlData
https://serpapi.com/maps-local-results
https://github.com/iewoai/GoogleMap_Spider/blob/master/main.py
https://medium.com/@supun1001/how-to-generate-google-embed-links-programmatically-for-iframes-for-routes-only-d6dc225e59e8
https://andrewwhitby.com/2014/09/09/google-maps-new-embed-format/

```
https://www.google.com/search?tbm=map&authuser=0....
{4: {'id': 4,
     'length': 12,
     'type': 'matrix',
     'value': {1: {'id': 1,
                   'length': 3,
                   'type': 'matrix',
                   'value': {1: {'id': 1,
                                 'type': 'double',
                                 'value': 739207.2818756471},
                             2: {'id': 2,
                                 'type': 'double',
                                 'value': 30.254350000000002},
                             3: {'id': 3,
                                 'type': 'double',
                                 'value': 26.69425}}},
               2: {'id': 2,
                   'length': 3,
                   'type': 'matrix',
                   'value': {1: {'id': 1, 'type': 'float', 'value': 0.0},
                             2: {'id': 2, 'type': 'float', 'value': 0.0},
                             3: {'id': 3, 'type': 'float', 'value': 0.0}}},
               3: {'id': 3,
                   'length': 2,
                   'type': 'matrix',
                   'value': {1: {'id': 1, 'type': 'integer', 'value': 1536},
                             2: {'id': 2, 'type': 'integer', 'value': 686}}},
               4: {'id': 4, 'type': 'float', 'value': 13.1}}},
               
 7: {'id': 7, 'type': 'integer', 'value': 20},
 8: {'id': 8, 'type': 'integer', 'value': 0},
 10: {'id': 10, 'type': 'boolean', 'value': True},
 12: {'id': 12,
      'length': 16,
      'type': 'matrix',
      'value': {1: {'id': 1,
                    'length': 1,
                    'type': 'matrix',
                    'value': {18: {'id': 18,
                                   'type': 'boolean',
                                   'value': True}}},
                2: {'id': 2,
                    'length': 3,
                    'type': 'matrix',
                    'value': {5: {'id': 5,
                                  'length': 1,
                                  'type': 'matrix',
                                  'value': {6: {'id': 6,
                                                'type': 'enum (as integer)',
                                                'value': 2}}},
                              20: {'id': 20,
                                   'type': 'enum (as integer)',
                                   'value': 3}}},
                10: {'id': 10, 'type': 'boolean', 'value': True},
                12: {'id': 12, 'type': 'boolean', 'value': True},
                13: {'id': 13, 'type': 'boolean', 'value': True},
                16: {'id': 16, 'type': 'boolean', 'value': True},
                17: {'id': 17,
                     'length': 1,
                     'type': 'matrix',
                     'value': {3: {'id': 3,
                                   'type': 'enum (as integer)',
                                   'value': 1}}},
                20: {'id': 20,
                     'length': 3,
                     'type': 'matrix',
                     'value': {5: {'id': 5,
                                   'type': 'enum (as integer)',
                                   'value': 2},
                               6: {'id': 6, 'type': 'boolean', 'value': True},
                               14: {'id': 14,
                                    'type': 'boolean',
                                    'value': True}}}}},
 19: {'id': 19,
      'length': 4,
      'type': 'matrix',
      'value': {2: {'id': 2,
                    'length': 3,
                    'type': 'matrix',
                    'value': {1: {'id': 1, 'type': 'integer', 'value': 360},
                              2: {'id': 2, 'type': 'integer', 'value': 120},
                              4: {'id': 4, 'type': 'integer', 'value': 8}}}}},
 20: {'id': 20,
      'length': 57,
      'type': 'matrix',
      'value': {2: {'id': 2,
                    'length': 2,
                    'type': 'matrix',
                    'value': {1: {'id': 1, 'type': 'integer', 'value': 203},
                              2: {'id': 2, 'type': 'integer', 'value': 100}}},
                3: {'id': 3,
                    'length': 2,
                    'type': 'matrix',
                    'value': {2: {'id': 2, 'type': 'integer', 'value': 4},
                              5: {'id': 5, 'type': 'boolean', 'value': True}}},
                6: {'id': 6,
                    'length': 6,
                    'type': 'matrix',
                    'value': {1: {'id': 1,
                                  'length': 2,
                                  'type': 'matrix',
                                  'value': {1: {'id': 1,
                                                'type': 'integer',
                                                'value': 408},
                                            2: {'id': 2,
                                                'type': 'integer',
                                                'value': 240}}}}},
                7: {'id': 7,
                    'length': 42,
                    'type': 'matrix',
                    'value': {1: {'id': 1,
                                  'length': 3,
                                  'type': 'matrix',
                                  'value': {1: {'id': 1,
                                                'type': 'enum (as integer)',
                                                'value': 10},
                                            2: {'id': 2,
                                                'type': 'boolean',
                                                'value': True},
                                            3: {'id': 3,
                                                'type': 'enum (as integer)',
                                                'value': 4}}},
                              2: {'id': 2, 'type': 'boolean', 'value': True},
                              4: {'id': 4, 'type': 'boolean', 'value': True}}},
                9: {'id': 9, 'type': 'boolean', 'value': True}}},
 22: {'id': 22,
      'length': 6,
      'type': 'matrix',
      'value': {1: {'id': 1,
                    'type': 'string',
                    'value': 'tRLSZM7lG--0kdUPh8SyiAM:4'},
                2: {'id': 2,
                    'type': 'string',
                    'value': '1i:0,t:11886,p:tRLSZM7lG--0kdUPh8SyiAM:4'},
                7: {'id': 7, 'type': 'enum (as integer)', 'value': 81},
                12: {'id': 12, 'type': 'enum (as integer)', 'value': 5},
                17: {'id': 17,
                     'type': 'string',
                     'value': 'tRLSZM7lG--0kdUPh8SyiAM:28'},
                18: {'id': 18, 'type': 'enum (as integer)', 'value': 15}}},
 24: {'id': 24,
      'length': 81,
      'type': 'matrix',
      'value': {1: {'id': 1,
                    'length': 29,
                    'type': 'matrix',
                    'value': {13: {'id': 13,
                                   'length': 9,
                                   'type': 'matrix',
                                   'value': {2: {'id': 2,
                                                 'type': 'boolean',
                                                 'value': True},
                                             3: {'id': 3,
                                                 'type': 'boolean',
                                                 'value': True},
                                             4: {'id': 4,
                                                 'type': 'boolean',
                                                 'value': True},
                                             6: {'id': 6,
                                                 'type': 'integer',
                                                 'value': 1},
                                             8: {'id': 8,
                                                 'type': 'boolean',
                                                 'value': True},
                                             9: {'id': 9,
                                                 'type': 'boolean',
                                                 'value': True},
                                             14: {'id': 14,
                                                  'type': 'boolean',
                                                  'value': True},
                                             20: {'id': 20,
                                                  'type': 'boolean',
                                                  'value': True},
                                             25: {'id': 25,
                                                  'type': 'boolean',
                                                  'value': True}}},
                              18: {'id': 18,
                                   'length': 18,
                                   'type': 'matrix',
                                   'value': {3: {'id': 3,
                                                 'type': 'boolean',
                                                 'value': True},
                                             4: {'id': 4,
                                                 'type': 'boolean',
                                                 'value': True},
                                             5: {'id': 5,
                                                 'type': 'boolean',
                                                 'value': True},
                                             6: {'id': 6,
                                                 'type': 'boolean',
                                                 'value': True},
                                             9: {'id': 9,
                                                 'type': 'boolean',
                                                 'value': True},
                                             12: {'id': 12,
                                                  'type': 'boolean',
                                                  'value': True},
                                             13: {'id': 13,
                                                  'type': 'boolean',
                                                  'value': True},
                                             14: {'id': 14,
                                                  'type': 'boolean',
                                                  'value': True},
                                             15: {'id': 15,
                                                  'type': 'boolean',
                                                  'value': True},
                                             17: {'id': 17,
                                                  'type': 'boolean',
                                                  'value': True},
                                             20: {'id': 20,
                                                  'type': 'boolean',
                                                  'value': True},
                                             21: {'id': 21,
                                                  'type': 'boolean',
                                                  'value': True},
                                             22: {'id': 22,
                                                  'type': 'boolean',
                                                  'value': True},
                                             25: {'id': 25,
                                                  'type': 'boolean',
                                                  'value': True},
                                             27: {'id': 27,
                                                  'length': 1,
                                                  'type': 'matrix',
                                                  'value': {1: {'id': 1,
                                                                'type': 'boolean',
                                                                'value': True}}},
                                             28: {'id': 28,
                                                  'type': 'boolean',
                                                  'value': True},
                                             30: {'id': 30,
                                                  'type': 'boolean',
                                                  'value': True}}}}},
                2: {'id': 2, 'type': 'boolean', 'value': True},
                5: {'id': 5,
                    'length': 5,
                    'type': 'matrix',
                    'value': {2: {'id': 2, 'type': 'boolean', 'value': True},
                              5: {'id': 5, 'type': 'boolean', 'value': True},
                              6: {'id': 6, 'type': 'boolean', 'value': True},
                              7: {'id': 7, 'type': 'boolean', 'value': True},
                              10: {'id': 10,
                                   'type': 'boolean',
                                   'value': True}}},
                10: {'id': 10,
                     'length': 1,
                     'type': 'matrix',
                     'value': {8: {'id': 8,
                                   'type': 'enum (as integer)',
                                   'value': 3}}},
                11: {'id': 11,
                     'length': 1,
                     'type': 'matrix',
                     'value': {3: {'id': 3,
                                   'type': 'enum (as integer)',
                                   'value': 1}}},
                14: {'id': 14,
                     'length': 1,
                     'type': 'matrix',
                     'value': {3: {'id': 3, 'type': 'boolean', 'value': True}}},
                17: {'id': 17, 'type': 'boolean', 'value': True},
                20: {'id': 20,
                     'length': 2,
                     'type': 'matrix',
                     'value': {1: {'id': 1,
                                   'type': 'enum (as integer)',
                                   'value': 6}}},
                24: {'id': 24, 'type': 'boolean', 'value': True},
                25: {'id': 25, 'type': 'boolean', 'value': True},
                26: {'id': 26, 'type': 'boolean', 'value': True},
                29: {'id': 29, 'type': 'boolean', 'value': True},
                30: {'id': 30,
                     'length': 1,
                     'type': 'matrix',
                     'value': {2: {'id': 2, 'type': 'boolean', 'value': True}}},
                36: {'id': 36, 'type': 'boolean', 'value': True},
                39: {'id': 39,
                     'length': 3,
                     'type': 'matrix',
                     'value': {2: {'id': 2,
                                   'length': 2,
                                   'type': 'matrix',
                                   'value': {2: {'id': 2,
                                                 'type': 'integer',
                                                 'value': 1},
                                             3: {'id': 3,
                                                 'type': 'integer',
                                                 'value': 1}}}}},
                43: {'id': 43, 'type': 'boolean', 'value': True},
                52: {'id': 52, 'type': 'boolean', 'value': True},
                54: {'id': 54,
                     'length': 1,
                     'type': 'matrix',
                     'value': {1: {'id': 1, 'type': 'boolean', 'value': True}}},
                55: {'id': 55, 'type': 'boolean', 'value': True},
                56: {'id': 56,
                     'length': 2,
                     'type': 'matrix',
                     'value': {1: {'id': 1, 'type': 'boolean', 'value': True},
                               3: {'id': 3, 'type': 'boolean', 'value': True}}},
                65: {'id': 65,
                     'length': 5,
                     'type': 'matrix',
                     'value': {3: {'id': 3,
                                   'length': 4,
                                   'type': 'matrix',
                                   'value': {1: {'id': 1,
                                                 'length': 3,
                                                 'type': 'matrix',
                                                 'value': {1: {'id': 1,
                                                               'length': 2,
                                                               'type': 'matrix',
                                                               'value': {1: {'id': 1,
                                                                             'type': 'integer',
                                                                             'value': 224},
                                                                         2: {'id': 2,
                                                                             'type': 'integer',
                                                                             'value': 298}}}}}}}}},
                71: {'id': 71, 'type': 'boolean', 'value': True},
                72: {'id': 72,
                     'length': 4,
                     'type': 'matrix',
                     'value': {1: {'id': 1,
                                   'length': 2,
                                   'type': 'matrix',
                                   'value': {3: {'id': 3,
                                                 'type': 'boolean',
                                                 'value': True},
                                             5: {'id': 5,
                                                 'type': 'boolean',
                                                 'value': True}}},
                               4: {'id': 4, 'type': 'boolean', 'value': True}}},
                89: {'id': 89, 'type': 'boolean', 'value': True},
                103: {'id': 103, 'type': 'boolean', 'value': True},
                113: {'id': 113, 'type': 'boolean', 'value': True}}},
 26: {'id': 26,
      'length': 4,
      'type': 'matrix',
      'value': {2: {'id': 2,
                    'length': 3,
                    'type': 'matrix',
                    'value': {1: {'id': 1, 'type': 'integer', 'value': 80},
                              2: {'id': 2, 'type': 'integer', 'value': 92},
                              4: {'id': 4, 'type': 'integer', 'value': 8}}}}},
 30: {'id': 30,
      'length': 28,
      'type': 'matrix',
      'value': {1: {'id': 1,
                    'length': 6,
                    'type': 'matrix',
                    'value': {1: {'id': 1,
                                  'length': 2,
                                  'type': 'matrix',
                                  'value': {1: {'id': 1,
                                                'type': 'integer',
                                                'value': 0},
                                            2: {'id': 2,
                                                'type': 'integer',
                                                'value': 666}}},
                              2: {'id': 2,
                                  'length': 2,
                                  'type': 'matrix',
                                  'value': {1: {'id': 1,
                                                'type': 'integer',
                                                'value': 1536},
                                            2: {'id': 2,
                                                'type': 'integer',
                                                'value': 686}}}}}}},
 34: {'id': 34,
      'length': 18,
      'type': 'matrix',
      'value': {2: {'id': 2, 'type': 'boolean', 'value': True},
                3: {'id': 3, 'type': 'boolean', 'value': True},
                4: {'id': 4, 'type': 'boolean', 'value': True},
                6: {'id': 6, 'type': 'boolean', 'value': True},
                8: {'id': 8,
                    'length': 6,
                    'type': 'matrix',
                    'value': {1: {'id': 1, 'type': 'boolean', 'value': True},
                              3: {'id': 3, 'type': 'boolean', 'value': True},
                              4: {'id': 4, 'type': 'boolean', 'value': True},
                              5: {'id': 5, 'type': 'boolean', 'value': True},
                              6: {'id': 6, 'type': 'boolean', 'value': True},
                              7: {'id': 7, 'type': 'boolean', 'value': True}}},
                9: {'id': 9, 'type': 'boolean', 'value': True},
                12: {'id': 12, 'type': 'boolean', 'value': True},
                14: {'id': 14, 'type': 'boolean', 'value': True},
                20: {'id': 20, 'type': 'boolean', 'value': True},
                23: {'id': 23, 'type': 'boolean', 'value': True},
                25: {'id': 25, 'type': 'boolean', 'value': True},
                26: {'id': 26, 'type': 'boolean', 'value': True}}},
 37: {'id': 37,
      'length': 1,
      'type': 'matrix',
      'value': {1: {'id': 1, 'type': 'enum (as integer)', 'value': 81}}},
 42: {'id': 42, 'type': 'boolean', 'value': True},
 47: {'id': 47, 'length': 0, 'type': 'matrix', 'value': {}},
 49: {'id': 49,
      'length': 7,
      'type': 'matrix',
      'value': {3: {'id': 3, 'type': 'boolean', 'value': True},
                6: {'id': 6,
                    'length': 2,
                    'type': 'matrix',
                    'value': {1: {'id': 1, 'type': 'boolean', 'value': True},
                              2: {'id': 2, 'type': 'boolean', 'value': True}}},
                7: {'id': 7,
                    'length': 2,
                    'type': 'matrix',
                    'value': {1: {'id': 1,
                                  'type': 'enum (as integer)',
                                  'value': 3},
                              2: {'id': 2,
                                  'type': 'boolean',
                                  'value': True}}}}},
 50: {'id': 50,
      'length': 4,
      'type': 'matrix',
      'value': {2: {'id': 2, 'type': 'enum (as integer)', 'value': 2},
                3: {'id': 3,
                    'length': 2,
                    'type': 'matrix',
                    'value': {1: {'id': 1, 'type': 'boolean', 'value': True},
                              3: {'id': 3,
                                  'type': 'boolean',
                                  'value': True}}}}},
 61: {'id': 61, 'type': 'boolean', 'value': True},
 67: {'id': 67,
      'length': 2,
      'type': 'matrix',
      'value': {7: {'id': 7, 'type': 'boolean', 'value': True},
                10: {'id': 10, 'type': 'boolean', 'value': True}}},
 69: {'id': 69, 'type': 'integer', 'value': 657}}

```
```

https://www.google.com/maps/place/{name}/@{},{},{}z/data=!4m6!3m5!1s0x14f9e3054ae0727f:0xde8f78c8fa6ac846!8m2!3d31.4519438!4d31.6843306!16s%2Fg%2F1pty8slyq?entry=ttu
!4m6!3m5!1s0x14f9e3054ae0727f:0xde8f78c8fa6ac846!8m2!3d31.4519438!4d31.6843306!16s%2Fg%2F1pty8slyq
!4m6!3m5!1s0x14f9e3054ae0727f:0xde8f78c8fa6ac846!8m2!3d31.4519438!4d31.6843306!16s/g/1pty8slyq
```

```python
var = {4: {'id': 4,
           'length': 6,
           'type': 'matrix',
           'value': {3: {'id': 3,
                         'length': 5,
                         'type': 'matrix',
                         'value': {1: {'id': 1,
                                       'type': 'string',
                                       'value': '0x14f9e3054ae0727f:0xde8f78c8fa6ac846'},
                                   8: {'id': 8,
                                       'length': 2,
                                       'type': 'matrix',
                                       'value': {3: {'id': 3,
                                                     'type': 'double',
                                                     'value': 31.4519438},
                                                 4: {'id': 4,
                                                     'type': 'double',
                                                     'value': 31.6843306}}},
                                   16: {'id': 16,
                                        'type': 'string',
                                        'value': '/g/1pty8slyq'
                                        }
                                   }
                         }
                     }
           }
       }
```
```
'0x14f9e3054ae0727f:0xde8f78c8fa6ac846'
1511488761830077055:16037169602679720006
```