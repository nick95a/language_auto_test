import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


language = 'es'

@pytest.fixture(scope = 'function')
def browser(language):
    
    browser = webdriver.Chrome()
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{language}/")
    yield browser
    browser.quit()
    
    