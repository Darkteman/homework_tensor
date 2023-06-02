from pages.base_page import BasePage
from locators.yandex_page_locators import Locators
import time
import requests


class YandexPage(BasePage):

    def is_name_category_in_search_field(self, category):
        name_category = category.text.lower()
        self.get_visible_object(Locators.SEARCH_FIELD_IMAGES).click()
        first_pos = self.get_visible_object(Locators.FIRST_SEARCH_POSITION)
        text_search_field = first_pos.text
        self.get_visible_object(Locators.OUTSIDE_FIELD).click()
        return name_category in text_search_field

    def download_image(self, image, filename):
        image_src = image.get_attribute('src')
        print(image_src)
        response = requests.get(image_src)
        with open(filename, 'wb') as img_file:
            img_file.write(response.content)

    def get_image_code(self, image):
        image_src = image.get_attribute('src')
        code_image = requests.get(image_src).content
        self.driver.implicitly_wait(10)
        return code_image
