from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
   
    button.click()
    browser.execute_script("window.scrollBy(0, 100);")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.ID, "answer")
    y_element .send_keys(y)
    button1 = browser.find_element(By.ID, "solve")
    button1.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert.text)
finally:  
    browser.quit()

# не забываем оставить пустую строку в конце файла

