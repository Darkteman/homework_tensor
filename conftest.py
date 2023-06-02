import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


INDEX_PAGE = 'https://ya.ru'


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.get(INDEX_PAGE)
    driver.maximize_window()
    yield driver
    driver.quit()
