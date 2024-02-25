from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderPage(BasePage):
    scooter_logo = [By.XPATH, ".//a[@href = '/']"]
    yandex_logo = [By.XPATH, ".//a[@href = '//yandex.ru']"]

    def click_to_scooter_logo(self):
        self.click_on_element(self.scooter_logo)

    def click_to_yandex_logo(self):
        self.click_on_element(self.yandex_logo)
