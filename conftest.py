from webbrowser import Chrome

import pytest
from selenium import webdriver
from services import loginPage
import time
@pytest.fixture()
def login():
    driver = webdriver.Chrome(executable_path=r"C:\Deepak\SeleniumFramework\chromedriver_win32\chromedriver.exe")
    driver.maximize_window()
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = Chrome(chrome_options=chrome_options)
    yield

@pytest.fixture()
def clear():
    print("my value is 40")