from url import MAIN_URL
from locators import LoginPageLocators, MainPageLocators, ProfilePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_profile_button_click_authorized_shows_profilepage(logged_in_driver):
    #Авторизироваться
    #Кликнуть на "Личный кабинет"
    logged_in_driver.find_element(*MainPageLocators.PROFILE_LINK).click() #Гиперссылка "Личный кабинет"

    shows_profilepage = WebDriverWait(logged_in_driver, 3).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_PAGE)) #Страница профиля

    assert shows_profilepage

def test_profile_button_click_unauthorized_shows_loginpage(driver):
    driver.get(MAIN_URL)

    #Кликнуть на "Личный кабинет"
    driver.find_element(*MainPageLocators.PROFILE_LINK).click() #Гиперссылка "Личный кабинет"

    shows_loginpage = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_FORM)) #Форма входа в аккаунт

    assert shows_loginpage
    