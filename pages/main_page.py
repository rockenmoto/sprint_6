import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    question_locator = [By.XPATH, ".//div[@id='accordion__heading-{}']"]
    answer_locator = [By.XPATH, ".//div[@id='accordion__panel-{}']"]

    top_button = [By.XPATH, './/button[contains(@class, "ra12g") and text() = "Заказать"]']
    bottom_button = [By.XPATH, './/button[contains(@class, "ra12g Button") and text() = "Заказать"]']

    @allure.step('Сравниваем вопрос с ответом из раздела "Вопросы о важном"')
    def check_answer_for_question(self, number_of_question, expected_result):
        method, locator = self.question_locator
        quest_locator = locator.format(number_of_question)
        method, locator = self.answer_locator
        answer_locator = locator.format(number_of_question)

        self.scroll_to_element((method, quest_locator))
        self.click_on_element((method, quest_locator))

        return self.get_text_element((method, answer_locator)) == expected_result

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_the_order_button(self, is_up_button):
        if is_up_button:
            self.click_on_element(self.top_button)
        else:
            self.scroll_to_element(self.bottom_button)
            self.click_on_element(self.bottom_button)
