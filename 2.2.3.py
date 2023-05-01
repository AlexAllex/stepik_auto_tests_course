from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Selectfrom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import math
import time


try:
    link = " https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number1_element = browser.find_element(By.ID, "num1")
    
    number_1 = number1_element.text
    print(number_1)
    number2_element= browser.find_element(By.ID, "num2")
    
    number_2 = number2_element.text
    print(number_2)
    summ = int(number_1) + int(number_2)
    print(summ)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))
    button = browser.find_element(By.CLASS_NAME, "btn") 
    button.click()
finally: 
    time.sleep(20)
    browser.quit()
# не забываем оставить пустую строку в конце


