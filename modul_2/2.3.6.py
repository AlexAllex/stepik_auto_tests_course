from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = " http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    #x_value = x_element.get_attribute('valuex')
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element .send_keys(y)
    button1 = browser.find_element(By.CLASS_NAME, "btn")
    button1.click()
finally:  
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла
