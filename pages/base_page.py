from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from services.logging.log_conf import logger
from services.text_messages import msg

LAG_TIME_VISIBLE_OBJECT = 10
LOCATOR_DATA_INDEX = 0
LOCATOR_NAME_INDEX = 1
INDEX_LAST_WINDOW = -1


class BasePage:
    """
    Описывает базовый класс страницы веб-сайта.
    """
    def __init__(self, driver):
        """
        Инициализирует экземпляр страницы.
        """
        self.driver = driver

    def get_visible_object(self, locator, timeout=LAG_TIME_VISIBLE_OBJECT):
        """
        Возвращает отобразившийся на странице объект.
        Явное ожидание по умолчанию составляет 10 сек.
        При отсутствии объекта возникает исключение с
        кодом ошибки соответствующим данному объекту.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator[LOCATOR_DATA_INDEX]))
        except TimeoutException:
            msg_error = (f'{msg["visible_object_error"]} '
                         f'"{locator[LOCATOR_NAME_INDEX]}"!')
            logger.error(msg_error)
            raise TimeoutException(msg_error)

    def press_enter(self, object):
        """
        Нажимает клавишу Enter при нахождении на заданном объекте.
        """
        object.send_keys(Keys.ENTER)

    def input_data_in_field(self, data, field):
        """
        Вводит данные в переданное поле.
        """
        field.send_keys(data)

    def get_url_last_page(self):
        """
        Возвращает URL-адрес последней открытой страницы.
        """
        last_window = self.driver.window_handles[INDEX_LAST_WINDOW]
        self.driver.switch_to.window(last_window)
        return self.driver.current_url

    def hover_cursor_to_element(self, object):
        """
        Перемещает курсор на объект без нажатия.
        """
        action = ActionChains(self.driver)
        action.move_to_element(object)
        action.perform()
