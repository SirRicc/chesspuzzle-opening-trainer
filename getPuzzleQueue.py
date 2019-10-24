import json
from os import path


with open("./openingLibary.json") as f:
    libary = json.load(f)

# TODO:
# map over openingLibary and replace
# all characters that messed with utf-8 ( Ö Ä Ü )
# to be able to really get all openings
# -> D90 Gr\u00fcnfeld Defense: Flohr Variation

#get basic openings
def getOpening(opening, depth):
    # TODO:
    # add inut validation and give user an output on how to use the right args
    gameCache = []
    for key, elem in libary.items():
        # TODO:
        # map over openingLibary and replace
        # all ":" with "," in all keys
        if key.find(opening) == 4 and key.count(",") == depth:
            # TODO:
            # change the way ids get appended to smother itterate over them
            gameCache.append(elem)

    print(gameCache)

    with open("./puzzleCache.json", 'w+') as file:
        json.dump(gameCache, file, indent=4)
        file.close()

getOpening("Queen's", 2)
