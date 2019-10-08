from selenium import webdriver
import json
import time

# driver = webdriver.Firefox()

with open("libary", "r") as f:
    libary = json.load(f)

#not implemented yet
# with open("puzzlesSolved", "w+") as ps:
#     puzzleHistory = json.load(ps)

#get basic openings
def getOpenings():
    for key, elem in libary.items():
        if key.find(",") == -1 & key.find(":") == -1:
            print( key + " ->  " + str(len(elem) +" basic openings" ))

#this will get all subvariations of the opening
def selectOpenings(opening):
    #gameCache will be passed into our gameloop later
    #check gameCache against ids already played -> when 
    gameCache = []
    for key, elem in libary.items():
        if key.find(opening) == 4:
            gameCache.append(elem)
    print(gameCache)

selectOpenings("Queen's Pawn Game")



#create gameloop

#get ids tested against puzzleHistory 

#open puzzle 

#search every x sec -> driver.find_element_by_class_name("half continue")
#wich gets created on event: puzzleSolved

#redirect to next puzzle 

#decide for a way to represent these openings for better usability
