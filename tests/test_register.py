from url import REGISTER_URL
from locators import RegisterPageLocators, LoginPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_register_password_6_or_more_success(driver, generate_email, generate_password):
    driver.get(REGISTER_URL)

    #Регистрация
    driver.find_element(*RegisterPageLocators.NAME_FIELD_REG).send_keys("Имя") #Поле "Имя"
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD_REG).send_keys(generate_email) #Поле Email
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD_REG).send_keys(generate_password) #Поле пароль
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click() #Кнопка "Зарегистрироваться"

    signup_success = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_FORM)) #Форма входа в аккаунт

    assert signup_success

def test_register_password_less_than_6_shows_error(driver, generate_email, generate_incorrect_password):
    driver.get(REGISTER_URL)

    #Регистрация
    driver.find_element(*RegisterPageLocators.NAME_FIELD_REG).send_keys("Имя") #Поле "Имя"
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD_REG).send_keys(generate_email) #Поле Email
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD_REG).send_keys(generate_incorrect_password) #Поле пароль
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click() #Кнопка "Зарегистрироваться"

    password_error = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)) #Сообщение об ошибке

    assert password_error

