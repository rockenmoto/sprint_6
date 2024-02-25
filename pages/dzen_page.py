from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class DzenPage(BasePage):
    dzen_header = [By.XPATH, './/div[@class = "trends-entry-desktop__title-3S"]']

    def check_dzen_page(self):
        self.switch_to_dzen_page()
        dzen_text = self.get_text_element(self.dzen_header)
        return dzen_text

    def switch_to_dzen_page(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
