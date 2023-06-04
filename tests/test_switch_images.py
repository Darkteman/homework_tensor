from pages.yandex_page import YandexPage
from locators.yandex_page_locators import Locators
from services.utils import are_images_identical
from services.text_messages import msg
from services.logging.log_conf import logger

YANDEX_IMAGE_SITE = 'https://yandex.ru/images/'


def test_switch_images(driver):
    """
    Тестирует процесс переходов на страницах Яндекса.
    Проверяет наличие объектов и смены изображений.
    """
    page = YandexPage(driver)
    logger.info(msg['second_test_start'])

    page.get_visible_object(Locators.SEARCH_FIELD).click()
    all_services = page.get_visible_object(Locators.ALL_SERVICES)
    logger.info(msg['all_services_succ'])

    all_services.click()
    page.get_visible_object(Locators.IMAGES_SECTION).click()
    new_url = page.get_url_last_page()
    assert YANDEX_IMAGE_SITE == new_url, logger.error(msg['url_images_err'])
    logger.info(msg['url_images_succ'])

    first_category = page.get_visible_object(Locators.FIRST_CATEGORY_IMAGES)
    first_category.click()
    comparison_result = page.is_name_category_in_search_field(first_category)
    assert comparison_result, logger.error(msg['name_category_err'])
    logger.info(msg['name_category_succ'])

    page.get_visible_object(Locators.FIRST_IMAGE).click()
    image = page.get_visible_object(Locators.IMAGE)
    page.download_image(image, 'image_1.png')
    logger.info(msg['first_image_succ'])

    page.hover_cursor_to_element(image)
    page.get_visible_object(Locators.NEXT_BUTTON).click()
    image = page.get_visible_object(Locators.IMAGE)
    page.download_image(image, 'image_2.png')
    comparison_result = are_images_identical('image_1.png', 'image_2.png')
    assert comparison_result is False, logger.error(msg['image_changed_err'])
    logger.info(msg['image_changed_succ'])

    page.get_visible_object(Locators.PREV_BUTTON).click()
    image = page.get_visible_object(Locators.IMAGE)
    page.download_image(image, 'image_3.png')
    comparison_result = are_images_identical('image_1.png', 'image_3.png')
    assert comparison_result, logger.error(msg['image_return_err'])
    logger.info(msg['image_return_succ'])

    logger.info(msg['second_test_finish'])
