from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_visible_object(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            print('Время ожидания истекло, запрошенный объект не найден.')

    def get_url_current_page(self):
        last_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(last_window)
        return self.driver.current_url
