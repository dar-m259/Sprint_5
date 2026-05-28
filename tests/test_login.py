from url import MAIN_URL, REGISTER_URL, FORGOT_PASS_URL
from locators import LoginPageLocators, MainPageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_login_log_via_auth_button_success(driver, auth):
    driver.get(MAIN_URL)

    #Авторизация
    driver.find_element(*MainPageLocators.AUTH_BUTTON).click() #Кнопка "Войти в аккаунт"
    driver.find_element(*LoginPageLocators.EMAIL_FIELD_LOG).send_keys(auth['login']) #Поле Email
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD_LOG).send_keys(auth['password']) #Поле Пароль
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click() #Кнопка "Войти"

    order_button_is_visible = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)) #Кнопка "Оформить заказ"

    assert order_button_is_visible

def test_login_log_via_profile_button_success(driver, auth):
    driver.get(MAIN_URL)

    #Авторизация
    driver.find_element(*MainPageLocators.PROFILE_LINK).click() #Гиперссылка "Личный кабинет"
    driver.find_element(*LoginPageLocators.EMAIL_FIELD_LOG).send_keys(auth['login']) #Поле Email
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD_LOG).send_keys(auth['password']) #Поле Пароль
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click() #Кнопка "Войти"

    order_button_is_visible = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)) #Кнопка "Оформить заказ"

    assert order_button_is_visible

def test_login_log_from_register_page_success(driver, auth):
    driver.get(REGISTER_URL)

    #Авторизация
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click() #Гиперссылка "Войти"
    driver.find_element(*LoginPageLocators.EMAIL_FIELD_LOG).send_keys(auth['login']) #Поле Email
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD_LOG).send_keys(auth['password']) #Поле Пароль
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click() #Кнопка "Войти"
  
    order_button_is_visible = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)) #Кнопка "Оформить заказ"

    assert order_button_is_visible

def test_login_log_from_passwordrecovery_page_succes(driver, auth):
    driver.get(FORGOT_PASS_URL)

    #Авторизация
    driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK_FP).click() #Гиперссылка "Войти"
    driver.find_element(*LoginPageLocators.EMAIL_FIELD_LOG).send_keys(auth['login']) #Поле Email
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD_LOG).send_keys(auth['password']) #Поле Пароль
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click() #Кнопка "Войти"

    order_button_is_visible = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)) #Кнопка "Оформить заказ"

    assert order_button_is_visible

