import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from services.utils import add_empty_line_in_logs

INDEX_PAGE = 'https://ya.ru'
LAG_TIME_PAGE_LOAD = 10


@pytest.fixture()
def driver():
    """
    Создает первичные настройки для запуска веб-драйвера Chrome.
    Передает фикстуры перед каждым тестом.
    """
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.get(INDEX_PAGE)
    driver.set_page_load_timeout(LAG_TIME_PAGE_LOAD)
    driver.maximize_window()
    yield driver
    add_empty_line_in_logs()
    driver.quit()
