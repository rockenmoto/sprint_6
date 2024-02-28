import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем элемент')
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step('Получаем текст элемента')
    def get_text_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Заполняем поле текстом')
    def fill_in_field(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    @allure.step('Переходим на другую страницу')
    def switch_to_next_tab(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
