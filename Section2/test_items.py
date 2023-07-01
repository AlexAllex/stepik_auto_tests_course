import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_should_see_button(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."
    browser.get(link)
    time.sleep(30)
   
    #button = browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    
    #assert button, 'no button'
    assert browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"), 'basket button not found'
