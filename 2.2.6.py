from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Selectfrom selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element = browser.find_element(By.ID, "input_value")
    
    x = element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element .send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    option1 = browser.find_element(By.ID, "robotCheckbox") 
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule") 
    option2.click()
    button = browser.find_element(By.CLASS_NAME, "btn") 
    button.click()
finally:  
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла

