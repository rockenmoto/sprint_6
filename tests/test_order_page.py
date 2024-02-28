import datetime

import pytest


class TestOrderPage:
    @pytest.mark.parametrize("is_up_button, name, last_name, address, metro, phone, delivery_date, rental_period",
                             [[True, 'Игорь', 'Лампов', 'Не дом и не улица', 'Чистые пруды', '+79224445577',
                               datetime.date.today().day, 'сутки'],
                              [False, 'Петруха', 'Котов', 'Советский Союз', 'Лубянка', '+798765551234',
                               datetime.date.today().day, 'трое суток']]
                             )
    def test_scooter_order_true(self, main_page, order_page, is_up_button, name, last_name,
                                address, metro, phone, delivery_date, rental_period):
        main_page.click_on_the_order_button(is_up_button)
        order_page.person_form(name, last_name, address, metro, phone)
        order_page.rent_form(delivery_date, rental_period)
        assert 'Заказ оформлен' in order_page.check_successful_order()
