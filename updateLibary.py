from selenium import webdriver
import json
import time


#start the emulated firefox 
driver = webdriver.Firefox()

#open json from file
with open("openingLibary", "r") as f:
    libary = json.load(f)

#checks last id from libary to progress from there
startNum = 0
for key, elem in libary.items():
    startNum = len(elem) + startNum


for x in range(startNum, 100000):
    #build url
    url = "https://lichess.org/training/"
    id = str(x)
    #merge incrementing html link and open
    driver.get(str(url+id))
    #find content on website
    variation = driver.find_element_by_class_name("opening_box")

    #logic to fill libary
    if variation.text in libary.keys() :
        libary[variation.text].append(id)
    else:
        libary[variation.text] = []
        libary[variation.text].append(id)


    #create a savegame
    with open('libary', 'w+') as file:
        json.dump(libary, file, indent=4)

    
    file.close()
    #time sleep 20 is required since Lichess only allows 1request/20sec
    time.sleep(20)
