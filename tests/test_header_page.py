class TestHeaderPage:
    def test_click_on_scooter_logo_true(self, header_page, main_page):
        main_page.click_on_the_order_button(True)
        header_page.click_to_scooter_logo()
        assert main_page.wait_for_element(main_page.bottom_button)
