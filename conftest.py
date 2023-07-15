import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


language = input("Enter the language")

@pytest.fixture(scope = "class")
def browser(language):
    browser = webdriver.Chrome()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{language}/"
    browser.get(link)
    yield browser
    browser.quit()
    