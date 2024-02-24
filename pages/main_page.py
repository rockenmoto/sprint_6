from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    question_locator = [By.XPATH, ".//div[@id='accordion__heading-{}']"]
    answer_locator = [By.XPATH, ".//div[@id='accordion__panel-{}']"]

    def check_answer_for_question(self, number_of_question, expected_result):
        method, locator = self.question_locator
        quest_locator = locator.format(number_of_question)
        method, locator = self.answer_locator
        answer_locator = locator.format(number_of_question)

        self.scroll_to_element((method, quest_locator))
        self.click_on_element((method, quest_locator))

        return self.get_text_element((method, answer_locator)) == expected_result
