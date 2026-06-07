import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=Service(), options=options)
    yield driver
    driver.quit()
