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
    
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    else:
        browser = None
        raise Exception("Browser should be chrome")
    
    if browser_language == 'es':
        """es_link = link + browser_language + "/"
        browser.get(es_link)
        """
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    elif browser_language == 'fr':
        fr_link = link + browser_language + "/"
        browser.get(fr_link)
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    else:
        browser.get(link)

    yield browser
    browser.quit()
    
    