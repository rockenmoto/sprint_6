class TestDzenPage:
    def test_click_on_dzen_logo_true(self, dzen_page, header_page):
        header_page.click_to_yandex_logo()
        assert dzen_page.check_dzen_page() == 'Тренды в Дзене'
