import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])


  


def test_autoriz(browser, links):
        browser.implicitly_wait(30)
        
        browser.get(links)
       
        button = browser.find_element(By.ID, "ember33")
        button.click()
        e_mail = browser.find_element(By.ID, "id_login_email")
        e_mail .send_keys("e-mail")
        parol = browser.find_element(By.ID, "id_login_password")
        parol.send_keys("password")
        button_enter = browser.find_element(By. CLASS_NAME, "sign-form__btn.button_with-loader ")
        
        button_enter.click()
        
        
        answer_fild = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
        answer =str( math.log(int(time.time())))
        answer_fild.send_keys(answer)
        print(answer)
      
        button1 = WebDriverWait(browser, 25).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button1.click()
        print('Buttom numeral clik')
        time.sleep(10)
        answer_stepik = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        answer_stepik = answer_stepik.text
        print(answer_stepik.text)
        
        assert"Correct!" in answer_stepik.text
      
        
        if answer_stepik != 'Correct!':
             with open('result.txt', 'a') as file:
                file.write (str(answer_stepik.text))
             file.close()

        button2 = WebDriverWait(browser, 25).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "again-btn.white")))
        if WebDriverWait(browser, 25).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "again-btn.white"))):
            button2 = browser.find_element(By.CLASS_NAME, "again-btn.white")
            

        
        button2.click()
        button3 = browser.find_element(By.CSS_SELECTOR, ".modal-popup__footer.ember-view > button:nth-child(1)")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
        #time.sleep(10)
        button3.click()
  






