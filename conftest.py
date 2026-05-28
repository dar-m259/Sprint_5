import pytest
import random

from faker import Faker
from url import LOGIN_URL
from locators import LoginPageLocators, MainPageLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def generate_email():
    faker = Faker()
    username = faker.password(length=random.randint(5, 10), special_chars=False, upper_case=False)
    domain = faker.free_email_domain()
    email = f"{username}@{domain}"
    return email

@pytest.fixture
def generate_password():
    faker = Faker()
    password = faker.password(length=random.randint(6, 12))
    return password

@pytest.fixture
def generate_incorrect_password():
    faker = Faker()
    password = faker.password(5)
    length = random.randint(1, 5)
    return password[::length]

@pytest.fixture
def auth():
    return {'login': 'dariamomatyuk46_123@ya.ru', 
            'password': 'sj76wgbkhk&^1'}

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver():
    driver = webdriver.Chrome()
    driver.get(LOGIN_URL)

    login = "dariamomatyuk46_123@ya.ru"
    password = "sj76wgbkhk&^1"

    #Авторизация
    driver.find_element(*LoginPageLocators.EMAIL_FIELD_LOG).send_keys(login) #Поле Email
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD_LOG).send_keys(password) #Поле Пароль
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click() #Кнопка "Войти"

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

    yield driver
    driver.quit()