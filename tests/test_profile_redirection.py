from locators import MainPageLocators, ProfilePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestProfileRedirection:
    def test_profile_redirection_click_constructor_shows_constructor(self, logged_in_driver):
        #Авторизироваться
        #Кликнуть на "Личный кабинет"
        logged_in_driver.find_element(*MainPageLocators.PROFILE_LINK).click() #Гиперссылка "Личный кабинет"

        #Кликнуть на "Конструкор"
        logged_in_driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).click() #Гиперссылка "Конструктор"

        shows_constructor = WebDriverWait(logged_in_driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR)) #Конструктор

        assert shows_constructor

    def test_profile_redirection_click_logo_shows_constructor(self, logged_in_driver):
        #Авторизироваться
        #Кликнуть на "Личный кабинет"
        logged_in_driver.find_element(*MainPageLocators.PROFILE_LINK).click() #Гиперссылка "Личный кабинет"

        #Кликнуть на Лого
        logged_in_driver.find_element(*ProfilePageLocators.LOGO).click() #Логотип

        shows_constructor = WebDriverWait(logged_in_driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR)) #Конструктор

        assert shows_constructor
    



