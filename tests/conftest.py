import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope="function")
def order_page(driver):
    return OrderPage(driver)
