import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
@pytest.mark.parametrize('language', ["es", "fr", "en"])
@pytest.mark.parametrize('browser_name', ["chrome", "firefox"])
"""

def test_add_to_cart_button(browser):

    time.sleep(30)
    add_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket")))
    assert add_button, "The button is not available"