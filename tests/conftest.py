import pytest
from selenium import webdriver
from pages.main_page import MainPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    driver.get("https://qa-scooter.praktikum-services.ru/")
    return MainPage(driver)
