from pages.base_page import BasePage
from locators.yandex_page_locators import Locators
import time
import requests

LAG_TIME_ON_IMAGE_LOAD = 1


class YandexPage(BasePage):
    """
    Расширяет базовый класс страницы веб-сайта.
    Добавляет функционал для страниц Яндекса.
    """
    def is_name_category_in_search_field(self, category):
        """
        Возвращает булево значения на основе результатов сравнения.
        Проверяет отобразилось ли названия категории картинок в поле поиска.
        Текст в поле поиска берется из первой ссылки окна подсказок.
        """
        name_category = category.text.lower()
        self.get_visible_object(Locators.SEARCH_FIELD_IMAGES).click()
        first_pos = self.get_visible_object(Locators.FIRST_SEARCH_POSITION)
        text_search_field = first_pos.text
        self.get_visible_object(Locators.OUTSIDE_FIELD).click()
        return name_category in text_search_field

    def download_image(self, image, filename):
        """
        Скачивает открытое изображение на странице.
        Сохраняет файл в корне директории проекта.
        Короткая временная задержка перед получением кода картинки
        исключает возможность скачивания файла уменьшенного формата.
        При необходимости время можно увеличить.
        """
        time.sleep(LAG_TIME_ON_IMAGE_LOAD)
        image_src = image.get_attribute('src')
        response = requests.get(image_src)
        with open(filename, 'wb') as img_file:
            img_file.write(response.content)
