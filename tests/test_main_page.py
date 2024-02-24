import pytest

from data import ExpectedAnswer


class TestMainPage:
    @pytest.mark.parametrize("number_of_question, expected_result",
                             [("0", ExpectedAnswer.answer_0),
                              ("1", ExpectedAnswer.answer_1),
                              ("2", ExpectedAnswer.answer_2),
                              ("3", ExpectedAnswer.answer_3),
                              ("4", ExpectedAnswer.answer_4),
                              ("5", ExpectedAnswer.answer_5),
                              ("6", ExpectedAnswer.answer_6),
                              ("7", ExpectedAnswer.answer_7)
                              ])
    def test_actual_answer_for_question_true(self, main_page, number_of_question, expected_result):
        assert main_page.click_to_question_and_check_answer(number_of_question, expected_result)
