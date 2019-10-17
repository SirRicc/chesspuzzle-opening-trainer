from selenium import webdriver


driver = webdriver.Firefox()

driver.get("https://www.google.com/")


def sandbox():
    if driver.find_element_by_id("hplogo") == True:
        print("true")
    else:
        print("false")


sandbox()
