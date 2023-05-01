from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element .send_keys(y)
    
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

    

    