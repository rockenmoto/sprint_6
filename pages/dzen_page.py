import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DzenPage(BasePage):
    dzen_header = [By.XPATH, './/div[@class = "trends-entry-desktop__title-3S"]']

    @allure.step('Проверяем открывшуюся страницу "Дзен"')
    def check_dzen_page(self):
        self.switch_to_next_tab()
        dzen_text = self.get_text_element(self.dzen_header)
        return dzen_text
