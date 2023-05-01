from selenium import webdriver
from selenium.webdriver.common.by import By

import time
link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"
robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
print(people_radio.get_attribute("checked"))

print(people_radio.get_attribute("href"))