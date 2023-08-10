import re
from urllib.parse import urlparse, parse_qs, unquote
import pprint


class GoogleMapsQueryArgsDeserializer:

    def decode_google_maps_url(self, url):
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        decoded_params = {}

        for key, values in query_params.items():
            decoded_values = []
            for value in values:
                decoded_value = unquote(value)
                decoded_values.append(decoded_value)
            decoded_params[key] = decoded_values if len(decoded_values) > 1 else decoded_values[0]

        pb = decoded_params.get("pb")
        pb_deserialize = self.deserialize(pb)
        decoded_params["pb_deserialize"] = pb_deserialize
        return decoded_params

    def deserialize(self, input_string):
        params = input_string.strip('!').split('!')

        for i in range(len(params)):
            params[i] = params[i].replace('%21', '!')  # URL-decode the param

        return self.decode(params)

    def decode(self, params):
        all_data = {}
        i = 0
        types = {
            "m": 'matrix',
            "f": 'float',
            "d": 'double',
            "i": "integer",
            "b": 'boolean',
            "e": 'enum (as integer)',
            "s": "string",
            'u': "unsigned int",
        }

        while i < len(params):
            param = params[i]
            if re.match(r'^(\d+)m(\d+)', param):
                matches = re.match(r'^(\d+)m(\d+)', param)
                id_ = int(matches.group(1))
                length = int(matches.group(2))
                var = {
                    "id": id_,
                    "length": length,
                    "type": types["m"],
                    "value": self.decode(params[i + 1:i + 1 + length])
                }
                # all_data[id] = GoogleMapsQueryArgsDeserializer.decode(params[i + 1:i + 1 + length])
                all_data[id_] = var
                i += length

            elif re.match(r'^(\d+)([fdibesuv])(.*)$', param):
                matches = re.match(r'^(\d+)([fdibesuv])(.*)$', param)
                id_ = int(matches.group(1))
                type_ = matches.group(2)
                value = matches.group(3)
                if type_ in ['i', 'e', 'u']:
                    value = int(value)
                elif type_ == 'f':
                    value = float(value)
                elif type_ == 'd':
                    value = float(value)
                elif type_ == 'b':
                    value = bool(value)
                elif type_ in ['s', 'v']:
                    value = str(value)
                else:
                    print(type_, "type not index")

                var = {
                    "id": id_,
                    "type": types[type_],
                    "value": value
                }
                all_data[id_] = var
            else:
                raise RuntimeError('Unknown param format: ' + param)

            i += 1

        return all_data

    def serialize(self, data):
        # TODO::
        types = {
            "m": 'matrix',
            "f": 'float',
            "d": 'double',
            "i": "integer",
            "b": 'boolean',
            "e": 'enum (as integer)',
            "s": "string",
            'u': "unsigned int",
        }
        types_rev = dict(zip(types.values(), types.keys()))

        params = []
        for id_, value in data.items():
            type_ = types_rev[value['type']]

            if type_ == 'm':
                length = value["length"]
                value_ = self.serialize(value['value'])

                if f"{id_}m{length}" == "1m2":
                    print(value_, value['value'])
                params.append(f'!{id_}m{length}{value_}')
                # params.extend(sub_params)
            elif type_ == 'b':
                value_ = int(value["value"])
                params.append(f'!{id_}{type_}{value_}')
            else:
                value_ = value["value"]
                if type_ == "f" and value_ == 0.0:
                    value_ = 0
                params.append(f'!{id_}{type_}{value_}')

        return ''.join(params)


#
url = ("https://www.google.com/search?tbm=map&authuser=0&hl=ar&gl=eg&q=مطعم في الرياض&oq=مطعم في الرياض&pb="
       "!4m12!1m3!1d739207.2818756471!2d30.254350000000002!3d26.69425!2m3!1f0!2f0!3f0!3m2!1i1536!2i686!4f13.1!7i20!8i0!10b1!12m16!1m1!18b1!2m3!5m1!6e2!20e3!10b1!12b1!13b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1stRLSZM7lG--0kdUPh8SyiAM%3A4!2s1i%3A0%2Ct%3A11886%2Cp%3AtRLSZM7lG--0kdUPh8SyiAM%3A4!7e81!12e5!17stRLSZM7lG--0kdUPh8SyiAM%3A28!18e15!24m81!1m29!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m18!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!25b1!27m1!1b0!28b0!30b0!2b1!5m5!2b1!5b1!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!103b1!113b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i50!2i686!1m6!1m2!1i1006!2i0!2m2!1i1536!2i686!1m6!1m2!1i0!2i0!2m2!1i1536!2i20!1m6!1m2!1i0!2i666!2m2!1i1536!2i686!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!47m0!49m7!3b1!6m2!1b1!2b1!7m2!1e3!2b1!50m4!2e2!3m2!1b1!3b1!61b1!67m2!7b1!10b1!69i657")
args = GoogleMapsQueryArgsDeserializer()
params = args.decode_google_maps_url(url)
# pprint.pprint(params.get("pb_deserialize"))
# print(args.serialize(params.get("pb_deserialize")))
# print(params.get("pb"))
"""

Hellow, in following part of url,

url:'!4m12!1m3!1d739207.2818756471!2d30.254350000000002!3d26.69425!2m3!1f0!2f0!3f0!3m2!1i1536!2i686!4f13.1!7i20!8i0!10b1!12m16!1m1!18b1!2m3!5m1!6e2!20e3!10b1!12b1!13b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m6!1stRLSZM7lG--0kdUPh8SyiAM:4!2s1i:0,t:11886,p:tRLSZM7lG--0kdUPh8SyiAM:4!7e81!12e5!17stRLSZM7lG--0kdUPh8SyiAM:28!18e15!24m81!1m29!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m18!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!25b1!27m1!1b0!28b0!30b0!2b1!5m5!2b1!5b1!6b1!7b1!10b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89'

some basic rules:

- url related to google maps search
- url consists of parameters, parameter is structure like "![id][type][value]" -> "!4m12" -> id=4, type=matrix, value=12, with types:
    '
    m: matrix
    f: float
    d: double
    i: integer
    b: boolean
    e: enum (as integer)
    s: string
    u: unsigned int
    '

- Matrices can encapsulate multiple data entries, e.g. !1m3!1i2!1i4!1i17 means that the matrix(m) with the ID 1 contains the three parameters [!1i2, !1i4, !1i17].

- parameters should related to latitude, range [-85.05112877980659, 85.05112877980659] and longitude, range [-180, 180] and zoom factor, range [2, 21]
- analyze some parameters:
    - '!1d739207.2818756471' > [id:1, type:double, value:739207.2818756471] represents latitude
    - '!2d30.254350000000002' > [id:2, type:double, value:30.254350000000002] represents longitude
    - '!3d26.69425' > [id:2, type:double, value:26.69425] represents zoom factor
    - '!7i20' > [id:7, type:integer, value:20] mean every page has 20 results
    - '!8i0' > [id:8, type:integer, value:0] mean start from result that has index 0
    
Please analyze all parameters(id, type, value) and interpret or guess their meaning, and if you can please output as json or table to easy read?
- output like `{id:id, type:type, meaning: your analyzes ,value: value}`
python class to deserialize url run GoogleMapsQueryArgsDeserializer.deserialize(url)
class GoogleMapsQueryArgsDeserializer:

    @staticmethod
    def deserialize(input_string):
        params = input_string.strip('!').split('!')

        for i in range(len(params)):
            params[i] = params[i].replace('%21', '!')  # URL-decode the param

        return GoogleMapsQueryArgsDeserializer.decode(params)

    @staticmethod
    def decode(params):
        data = {}
        i = 0

        while i < len(params):
            param = params[i]

            if re.match(r'^(\d+)m(\d+)', param):
                matches = re.match(r'^(\d+)m(\d+)', param)
                id = int(matches.group(1))
                length = int(matches.group(2))
                data[id] = GoogleMapsQueryArgsDeserializer.decode(params[i + 1:i + 1 + length])
                i += length
            elif re.match(r'^(\d+)([fdibesuv])(.*)$', param):
                matches = re.match(r'^(\d+)([fdibesuv])(.*)$', param)
                id = int(matches.group(1))
                type = matches.group(2)
                value = matches.group(3)
                if type in ['i', 'e', 'u']:
                    data[id] = int(value)
                elif type == 'f':
                    data[id] = float(value)
                elif type == 'd':
                    data[id] = float(value)
                elif type == 'b':
                    data[id] = bool(value)
                elif type in ['s', 'v']:
                    data[id] = str(value)
            else:
                raise RuntimeError('Unknown param format: ' + param)

            i += 1

        return data
"""

"""
the following python class name `GoogleMapsQueryArgsDeserializer` has method `deserialize` to deserialize or decode url
```python
import re
from urllib.parse import urlparse, parse_qs, unquote

class GoogleMapsQueryArgsDeserializer:

    @staticmethod
    def deserialize(input_string):
        params = input_string.strip('!').split('!')

        for i in range(len(params)):
            params[i] = params[i].replace('%21', '!')  # URL-decode the param

        return GoogleMapsQueryArgsDeserializer.decode(params)

    @staticmethod
    def decode(params):
        all_data = {}
        i = 0
        types = {
            "m": 'matrix',
            "f": 'float',
            "d": 'double',
            "i": "integer",
            "b": 'boolean',
            "e": 'enum (as integer)',
            "s": "string",
            'u': "unsigned int",
        }

        while i < len(params):
            param = params[i]
            if re.match(r'^(\d+)m(\d+)', param):
                matches = re.match(r'^(\d+)m(\d+)', param)
                id_ = int(matches.group(1))
                length = int(matches.group(2))
                var = {
                    "id": id_,
                    "length": length,
                    "type": types["m"],
                    "value": GoogleMapsQueryArgsDeserializer.decode(params[i + 1:i + 1 + length])
                }
                # all_data[id] = GoogleMapsQueryArgsDeserializer.decode(params[i + 1:i + 1 + length])
                all_data[id_] = var
                i += length

            elif re.match(r'^(\d+)([fdibesuv])(.*)$', param):
                matches = re.match(r'^(\d+)([fdibesuv])(.*)$', param)
                id_ = int(matches.group(1))
                type_ = matches.group(2)
                value = matches.group(3)
                if type_ in ['i', 'e', 'u']:
                    value = int(value)
                elif type_ == 'f':
                    value = float(value)
                elif type_ == 'd':
                    value = float(value)
                elif type_ == 'b':
                    value = bool(value)
                elif type_ in ['s', 'v']:
                    value = str(value)

                var = {
                    "id": id_,
                    "type": types[type_],
                    "value": value
                }
                all_data[id_] = var
            else:
                raise RuntimeError('Unknown param format: ' + param)

            i += 1

        return all_data
```

can create method serialize url to origin
"""
