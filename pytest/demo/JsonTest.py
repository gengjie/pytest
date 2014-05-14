__author__ = 'gengjie'
import json
import types

jsonStr = '{"name" : "gengjie", "age" :18, "html" : "<b>234234<\/b>"}'

print repr(json.dumps(jsonStr))

jsonfile = open("./json.txt")
str = jsonfile.read()
dict = json.JSONDecoder().decode(str)
for K, V in dict.items():
    print K, ":", V
    if type(V) == types.ListType:
        for E in V:
            if type(E) == types.DictionaryType:
                for k, v in E.items():
                    print '\t' * 5, k, ':', v
            print '\n'
jsonfile.close()
