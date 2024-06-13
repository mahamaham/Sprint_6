import allure

from helps.data import Users
from pages.home_page import HomePage, HomePageHeader
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Позитивный тест оформления заказа по клику на кнопку "Заказать" в хедере')
    @allure.description('''1)На главной странице в хедере кликаем на кнопку "Заказать";
                        2)Заполняем данные на странице "Для кого самокат' и кликаем на кнопку "Далее";
                        3)Заполняем данные "Про аренду" и кликаем на кнопку "Заказать";
                        4)Подтверждаем заказ и проверяем открытие окна с текстом оформления заказа''')
    def test_order_scooter_by_order_button_from_header(self, driver):
        header_page = HomePageHeader(driver)
        order_page = OrderPage(driver)
        header_page.order_button_click()
        order_page.order_scooter_full_path(Users.user)
        assert order_page.check_order_title()

    @allure.title('Позитивный тест оформления заказа по клику на кнопку "Заказать" на главной странице')
    @allure.description('''1)На главной странице скролл до кнопки "Заказать" и кликаем на нее;
                        2)Заполняем данные на странице "Для кого самокат' и кликаем на кнопку "Далее";
                        3)Заполняем данные "Про аренду" и кликаем на кнопку "Заказать";
                        4)Подтверждаем заказ и проверяем открытие окна с текстом оформления заказа''')
    def test_order_scooter_by_order_button_from_home_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.scroll_and_click_on_the_order_button()
        order_page.order_scooter_full_path(Users.user_2)
        assert order_page.check_order_title()
        