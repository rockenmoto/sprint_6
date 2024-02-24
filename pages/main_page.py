from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    question_locator = [By.XPATH, ".//div[@id='accordion__heading-{}']"]
    answer_locator = [By.XPATH, ".//div[@id='accordion__panel-{}']"]

    def click_to_question_and_check_answer(self, q_num, expected_result):
        method, locator = self.question_locator
        locator_q = locator.format(q_num)
        method, locator = self.answer_locator
        locator_a = locator.format(q_num)

        self.scroll_to_element((method, locator_q))
        self.click_on_element((method, locator_q))
        self.get_text_element((method, locator_a))

        return self.get_text_element((method, locator_a)) == expected_result
