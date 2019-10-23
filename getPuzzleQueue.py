from selenium import webdriver
import json
import time
import sys
from os import path


# driver = webdriver.Firefox()

with open(path.join(path.dirname(__file__), "openingLibary.json")) as f:
    libary = json.load(f)

# with open(path.join(path.dirname(__file__), "puzzleCache.json")) as c:
#     cache = json.load(c)


#get basic openings
def getOpening(opening, depth):
    # TODO:
    # add inut validation and gives user an output on how to use the right args
    gameCache = []
    for key, elem in libary.items():
        if key.find(opening) == 4 and key.count(":") == depth:
            gameCache.append(elem)

    # http://python.robasworld.com/python-relative-path/

    print(gameCache)

        #
        #   Dump it right & find a better way than using an absolute path
        #

#     with open('F:\dev\python\chesspuzzle-opening-trainer\puzzleCache.json', 'w+') as file:
#         json.dump(gameCache, file, indent=4)
#         file.close()
#
getOpening("Queen's", 2)






#not working
def startPuzzle(gameCache):
    puzzleSolveState = False
    for x in gameCache:
        url = "https://lichess.org/training/"
        id = str(x)
        while puzzleSolveState != True:
            variation = driver.find_element_by_class_name("opening_box")



# if __name__ == "__main__":
#     opening = str(sys.argv[1])
#     #may add an second argument to toggle true opening / opening with all variations
#     getOpening(opening)


# TODO:
    #create gameloop
    #get ids tested against puzzleHistory
    #open puzzle
    #event listener in while loop
        #search every x sec -> driver.find_element_by_class_name("half continue")
        #wich gets created on event: puzzleSolved
    #redirect to next puzzle
    #decide for a way to represent these openings for better usability
