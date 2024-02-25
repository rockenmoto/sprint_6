from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    order_page_title = [By.XPATH, ".//div[text() = 'Для кого самокат']"]
    about_rent_title = [By.XPATH, ".//div[text() = 'Про аренду']"]
    order_placed_title = [By.XPATH, './/div[text() = "Заказ оформлен"]']

    calendar_chooser = [By.XPATH, ".//div[text()={}]"]
    rental_period_chooser = [By.XPATH, ".//div[text()='{}']"]
    metro_value = [By.XPATH, ".//button/div[text()='{}']"]

    next_button = [By.XPATH, ".//button[text() = 'Далее']"]
    bottom_button = [By.XPATH, './/button[contains(@class, "ra12g Button") and text() = "Заказать"]']
    yes_button = [By.XPATH, './/button[text() = "Да"]']
    show_status_button = [By.XPATH, './/button[text() = "Посмотреть статус"]']

    name_field = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    last_name_field = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    address_field = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    metro_field = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    phone_field = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    delivery_date_field = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    rental_period_field = [By.XPATH, ".//div[text() = '* Срок аренды']"]

    def person_form(self, name, last_name, address, metro, phone):
        self.wait_for_element(self.order_page_title)
        self.fill_in_field(self.name_field, name)
        self.fill_in_field(self.last_name_field, last_name)
        self.fill_in_field(self.address_field, address)
        self.select_metro_station(metro)
        self.fill_in_field(self.phone_field, phone)
        self.click_on_element(self.next_button)

    def rent_form(self, delivery_date, rental_period):
        self.wait_for_element(self.about_rent_title)
        self.select_date_from_calendar(delivery_date)
        self.select_rental_period(rental_period)
        self.click_on_element(self.bottom_button)

    def check_successful_order(self):
        self.click_on_element(self.yes_button)
        successful_text = self.get_text_element(self.order_placed_title)
        self.click_on_element(self.show_status_button)
        return successful_text

    def select_metro_station(self, metro):
        method, locator = self.metro_value
        metro_locator = locator.format(metro)

        self.click_on_element(self.metro_field)
        self.scroll_to_element((method, metro_locator))
        self.click_on_element((method, metro_locator))

    def select_date_from_calendar(self, delivery_date):
        method, locator = self.calendar_chooser
        date = locator.format(delivery_date)

        self.click_on_element(self.delivery_date_field)
        self.click_on_element((method, date))

    def select_rental_period(self, rental_period):
        method, locator = self.rental_period_chooser
        period = locator.format(rental_period)

        self.click_on_element(self.rental_period_field)
        self.scroll_to_element((method, period))
        self.click_on_element((method, period))
