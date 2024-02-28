import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderPage(BasePage):
    scooter_logo = [By.XPATH, ".//a[@href = '/']"]
    yandex_logo = [By.XPATH, ".//a[@href = '//yandex.ru']"]

    @allure.step('Клик на логотип "Самокат"')
    def click_to_scooter_logo(self):
        self.click_on_element(self.scooter_logo)

    @allure.step('Клик на логотип "Яндекс"')
    def click_to_yandex_logo(self):
        self.click_on_element(self.yandex_logo)
