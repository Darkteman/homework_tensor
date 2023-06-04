from locators.yandex_page_locators import Locators
from pages.yandex_page import YandexPage
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

    page.input_data_in_field(TENSOR_INPUT, search_field)
    page.get_visible_object(Locators.SUGGEST_LIST)
    logger.info(msg['suggest_list_succ'])

    page.press_enter(search_field)
    page.get_visible_object(Locators.SEARCH_RESULT)
    logger.info(msg['search_result_succ'])

    page.get_visible_object(Locators.FIRST_LINK).click()
    new_url = page.get_url_last_page()
    assert TENSOR_SITE in new_url, logger.error(msg['tensor_site_err'])
    logger.info(msg['tensor_site_succ'])

    logger.info(msg['first_test_finish'])
