from locators import LoginPageLocators, MainPageLocators, ProfilePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_logout_success(logged_in_driver):
    #Авторизоваться
    #Кликнуть на "Личный кабинет"
    logged_in_driver.find_element(*MainPageLocators.PROFILE_LINK).click() #Гиперссылка "Личный кабинет"

    #Кликнуть на "Выход"
    logged_in_driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click() #Кнопка "Выход"

    logout_success = WebDriverWait(logged_in_driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_FORM)) #Форма входа в аккаунт

    assert logout_success
    