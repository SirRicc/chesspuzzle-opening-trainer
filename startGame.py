from selenium import webdriver
import json
import time
import sys

# driver = webdriver.Firefox()

with open("./openingLibary.json", "r") as f:
    libary = json.load(f)

#not implemented yet
# with open("puzzlesSolved", "w+") as ps:
#     puzzleHistory = json.load(ps)

#get basic openings
def getOpening(opening):
    gameCache = []
    for key, elem in libary.items():
        if key.find(",") == -1 & key.find(":") == -1:
            gameCache.append(elem)
            # print( key + " ->  " + str(len(elem) +" basic openings" ))

#this will get all subvariations of the opening
def getOpenings(opening):
    #gameCache will be passed into our gameloop later
    #check gameCache against ids already played -> when
    gameCache = []
    for key, elem in libary.items():
        if key.find(opening) == 4:
            gameCache.append(elem)
    print(gameCache)
    startPuzzle(gameCache)

# def awaitSolve():
#     pass
#
# def sandbox():
#     if
# print(driver.find_element_by_class_name("x"))

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



#create gameloop

#get ids tested against puzzleHistory

#open puzzle

#event listener in while loop
    #search every x sec -> driver.find_element_by_class_name("half continue")
    #wich gets created on event: puzzleSolved

#redirect to next puzzle

#decide for a way to represent these openings for better usability
