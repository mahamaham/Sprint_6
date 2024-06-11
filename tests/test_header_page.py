import time
import allure
import pytest

from helps.data import Questions, Urls
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage, HomePageHeader
from pages.dzen_page import DzenPage


class TestMainPage:

    @allure.title('Тест проверки перехода на главную страницу веб-приложения по клику на логотип "Самокат"')
    @allure.description('''1)Кликаем на кнопку "Заказать"
                        2)Кликаем на логотип "Самокат"
                        3)Сравниваем текущий URL с ожидаемым и отображение надписи - "Учебный проект"''')
    def test_scooter_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        header_page.order_button_click()
        header_page.scooter_logo_click()
        time.sleep(7)
        current_url = header_page.get_current_url()
        title_is_displayed = header_page.check_order_title()
        assert current_url == Urls.QA_SCOOTER_URL and title_is_displayed

    @allure.title('Тест проверки перехода на главную страницу DZEN по клику на логотип "Яндекс"')
    @allure.description('''1)Кликаем на логотип "Яндекс"
                        2)Переключаемся на новую вкладку и ждем загрузку страницы
                        3)Сравниваем текущий URL с ожидаемым''')
    def test_yandex_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        dzen_page = DzenPage(driver)
        header_page.yandex_logo_click()
        header_page.go_to_new_tab()
        time.sleep(7)
        current_url = header_page.get_current_url()
        assert current_url == Urls.DZEN_URL and dzen_page.check_element_main_button()

    @allure.title('Тест проверки текста ответов на вопросы на главной странице веб-приложения')
    @allure.description('''1)Скроллим до блока с вопросами;
                        2)Кликаем на вопрос;
                        3)Получаем текст ответа на выбранный вопрос;
                        4)Сравниваем полученный текст с ожидаемым''')
    @pytest.mark.parametrize('question_locator, question_text_locator, expected_question_text', zip(HomePageLocators.questions, HomePageLocators.questions_text, Questions.expected_question_text))
    def test_accordion(self, driver, question_locator, question_text_locator, expected_question_text):
        home_page = HomePage(driver)
        text = home_page.get_text_question(question_locator, question_text_locator)

        assert text == expected_question_text
        
