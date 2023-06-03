import time
from pages.yandex_page import YandexPage
from locators.yandex_page_locators import Locators
from selenium.webdriver.common.keys import Keys


TENSOR_SITE = 'https://tensor.ru/'
TENSOR_INPUT = 'Тензор'


def test_search_tensor(driver):
    page = YandexPage(driver)
    time.sleep(20)

    search_field = page.get_visible_object(Locators.SEARCH_FIELD)
    assert search_field, 'Поле поиска не найдено!'

    search_field.send_keys(TENSOR_INPUT)
    suggest_list = page.get_visible_object(Locators.SUGGEST_LIST)
    assert suggest_list, 'Таблица с подсказками не отобразилась!'

    search_field.send_keys(Keys.ENTER)
    search_result = page.get_visible_object(Locators.SEARCH_RESULT)
    assert search_result, 'Результы поиска не появились!'

    page.get_visible_object(Locators.FIRST_LINK).click()
    new_url = page.get_url_current_page()
    assert TENSOR_SITE in new_url, 'Первая ссылка не ведет на сайт Тензора!'
