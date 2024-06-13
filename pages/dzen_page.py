from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators
import allure
from selenium.webdriver.support import expected_conditions as EC


class DzenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка отображения кнопки "Главная" на странице DZEN')
    def check_element_main_button(self):
        return self.wait.until(EC.presence_of_element_located(DzenPageLocators.main_button_dzen))
