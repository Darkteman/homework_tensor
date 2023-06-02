import time
from pages.yandex_page import YandexPage
from locators.yandex_page_locators import Locators
from selenium.webdriver import ActionChains


YANDEX_IMAGE_SITE = 'https://yandex.ru/images/'


def test_switch_images(driver):
    page = YandexPage(driver)
    time.sleep(20)

    page.get_visible_object(Locators.SEARCH_FIELD).click()
    all_services = page.get_visible_object(Locators.ALL_SERVICES)
    assert all_services, 'Кнопка "Все сервисы" отсутствует на странице!'

    all_services.click()
    page.get_visible_object(Locators.IMAGES_SECTION).click()
    new_url = page.get_url_current_page()
    assert YANDEX_IMAGE_SITE == new_url, 'Перешли не на url Картинок.'

    first_category = page.get_visible_object(Locators.FIRST_CATEGORY_IMAGES)
    first_category.click()
    comparison_result = page.is_name_category_in_search_field(first_category)
    assert comparison_result is True, ('Название категории не '
                                       'отображается в поле поиска!')

    page.get_visible_object(Locators.FIRST_IMAGE).click()
    image = page.get_visible_object(Locators.IMAGE)
    assert image, 'Первая картинка не открылась!'
    code_first_image = page.get_image_code(image)
    page.download_image(image, 'image_1.png')

    ActionChains(page.driver).move_to_element(image).perform()
    page.get_visible_object(Locators.NEXT_BUTTON).click()
    image = page.get_visible_object(Locators.IMAGE)
    code_second_image = page.get_image_code(image)
    page.download_image(image, 'image_2.png')
    assert code_first_image != code_second_image, 'Картинка не сменилась!'

    page.get_visible_object(Locators.PREV_BUTTON).click()
    image = page.get_visible_object(Locators.IMAGE)
    code_third_image = page.get_image_code(image)
    page.download_image(image, 'image_3.png')
    assert code_first_image == code_third_image, ('При возврате назад картинка'
                                                  'отличается от изначальной!')
