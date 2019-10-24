#Thats my place to isolate and test features
from os import path
import os
import json




# test = {
#     "dummy" : "data3"
# }
test = {
    "dummy" : "data3"
}
#     json.dump(test, cache, indent="4")

# with open(path.join(path.dirname(__file__), "puzzleCache.json")) as x:
#
#
with open('./libarasdfAAAy.json', 'w+') as file:
    json.dump(test, file, indent=4)
