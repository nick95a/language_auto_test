import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('language', ["es", "fr"])
def test_add_to_cart_button(browser, language):
    
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{language}/")
    time.sleep(30)
    add_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket")))
    assert add_button, "The button is not available"