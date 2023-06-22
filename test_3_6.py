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
                                   "https://stepik.org/lesson/236896/step/1",])
                                  # "https://stepik.org/lesson/236897/step/1",
                                  # "https://stepik.org/lesson/236898/step/1",
                                  # "https://stepik.org/lesson/236899/step/1",
                                   #"https://stepik.org/lesson/236903/step/1",
                                   #"https://stepik.org/lesson/236904/step/1",
                                   #"https://stepik.org/lesson/236905/step/1"])


class Testsend:
  


    def test_autoriz( self, browser, links):
        browser.implicitly_wait(20)
        link = f"https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        browser.implicitly_wait(20)
        button = browser.find_element(By.ID, "ember33")
        button.click()
        e_mail = browser.find_element(By.ID, "id_login_email")
        e_mail .send_keys("aae199705@gmail.com")
        parol = browser.find_element(By.ID, "id_login_password")
        parol.send_keys("aniuta")
        button_enter = browser.find_element(By. CLASS_NAME, "sign-form__btn.button_with-loader ")
        #time.sleep(10)
        button_enter.click()
        
        #button2 = WebDriverWait(browser, 25).until(
        #EC.element_to_be_clickable((By.CLASS_NAME, "again-btn.white")))

        
        #button2.click()
        #button3 = browser.find_element(By.CSS_SELECTOR, ".modal-popup__footer.ember-view > button:nth-child(1)")
        #browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
        #time.sleep(10)
        #button3.click()
        answer =str( math.log(int(time.time())))
        link = links
        browser.get(link)
        #browser.implicitly_wait(20)
        answer_fild = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
        answer_fild.send_keys(answer)
        print(answer)
        #browser.implicitly_wait(10)
        button1 = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button1.click()
        answer_stepik = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        #WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "mart-hints__hint"))).Correct!
        #assert answer_stepik == "Correct!"
        #f"Wrong language, got {catalog_text} instead of 'Каталог'" 
        assert"Correct!" in answer_stepik.text
        #assert "Correct!" == answer_stepik, f'expected {Correct!}, got {test}'
        print(answer_stepik)
        if answer_stepik != 'Correct!':
            with open('result.txt', 'a') as file:
                file.write(answer_stepik)





   






