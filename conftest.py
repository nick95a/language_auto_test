import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


"""
language = 'es'
options.add_experimental_option('prefs', {'intl.accept_languages': language})
"""

options = Options()
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def pytest_addoption(parser):
    parser.addoption('--browser_name', action = 'store', default = 'chrome',
                      help = "Input your browser")
    parser.addoption('--language', action = 'store', default = 'es', 
                     help = 'Input your language')

@pytest.fixture(scope = 'function')
def browser(request):
    
    browser_name = request.config.getoption('browser_name')
    browser_language = request.config.getoption('language')
    browser = None
    
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})

    if browser_name == 'chrome':
        browser = webdriver.Chrome(options = options)
    else:
        browser = None
        raise pytest.UsageError("browser is not chrome")
    
    browser.get(link)
    
    yield browser
    browser.quit()
    
    