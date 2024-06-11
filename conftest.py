import allure
import pytest
from selenium import webdriver

from helps.data import Urls


@allure.step('Открытие браузера / переход на страницу сервиса / закрытие браузера')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.QA_SCOOTER_URL)
    yield driver
    driver.quit()


# Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val):
    return repr(val)