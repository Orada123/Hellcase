from selenium import webdriver
import time
import json

PATH = "/Applications/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://hellcase.com/en")

# To be saved into the json file
items = {}
num = list(range(1, 100))
count =  0
# Perpetual loop
while count <= 10:
    time.sleep(3)
    # Checks the rows for the user id  and  weapon name
    for i in range(1, 4): # Total number of divs is 17 need +1
        # Gets weapon name
        weapon = driver.find_element_by_xpath('//*[@id="live_drop"]/div[4]/div/div[' + str(i) + ']/a/div[1]')
        weapon_full = weapon.text.replace("\n", " ")

        # Gets  user id
        identifier = driver.find_element_by_xpath('// *[ @ id = "live_drop"] / div[4] / div / div[' + str(i) + '] / a').get_attribute("href")

        # Checks if the weapon text is filled
        if weapon_full != "" or '':
            # Adds the weapon to items dictionary
            if identifier not in items.keys():
                items[identifier] = weapon_full
            if identifier in items.keys() and weapon_full not in items.values():
                i = 0
                number = num[i]
                items[identifier + '(' + str(number) + ')'] = weapon_full
                num.remove(number)
                count += 1
                print(count)


file_name = "Hellcase-1.json"
with open(file_name, "w") as f_obj:
    json.dump(items, f_obj)  # Converts to string
    print(len(items))


