from pages.yandex_page import YandexPage
from locators.yandex_page_locators import Locators
from selenium.webdriver.common.keys import Keys
from services.logging.log_conf import logger
from services.text_messages import msg

TENSOR_SITE = 'https://tensor.ru/'
TENSOR_INPUT = 'Тензор'


def test_search_tensor(driver):
    """
    Тестирует процесс поиска на странице Яндекса.
    Проверяет наличие объектов и переход на сайт компании Тензор.
    """
    page = YandexPage(driver)
    logger.info(msg['first_test_start'])

    search_field = page.get_visible_object(Locators.SEARCH_FIELD)
    logger.info(msg['search_field_succ'])

    search_field.send_keys(TENSOR_INPUT)
    page.get_visible_object(Locators.SUGGEST_LIST)
    logger.info(msg['suggest_list_succ'])

    search_field.send_keys(Keys.ENTER)
    page.get_visible_object(Locators.SEARCH_RESULT)
    logger.info(msg['search_result_succ'])

    page.get_visible_object(Locators.FIRST_LINK).click()
    new_url = page.get_url_last_page()
    assert TENSOR_SITE in new_url, logger.error(msg['tensor_site_err'])
    logger.info(msg['tensor_site_succ'])

    logger.info(msg['first_test_finish'])
