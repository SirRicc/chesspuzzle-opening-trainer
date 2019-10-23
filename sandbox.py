#Thats my place to isolate and test features
from os import path
import json


# with open(path.join(path.dirname(__file__), "openingLibary.json")) as f:
#     libary = json.load(f)
#


path = with open(path.join(path.dirname(__file__), "puzzleCache.json")) as c:
    cache = json.load(c)

print(path)


# test = {
#     "dummy" : "data3"
# }
#     json.dump(test, cache, indent="4")

# with open(path.join(path.dirname(__file__), "puzzleCache.json")) as x:
