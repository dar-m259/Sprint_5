from selenium.webdriver.common.by import By

class RegisterPageLocators:     #Регистрация
    NAME_FIELD_REG = (By.XPATH, ".//label[text()='Имя']/parent::div/input") #Поле "Имя"
    EMAIL_FIELD_REG = (By.XPATH, ".//label[text()='Email']/parent::div/input") #Поле "Email"
    PASSWORD_FIELD_REG = (By.NAME, "Пароль") #Поле "Пароль"
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".button_button_size_medium__3zxIa") #Кнопка "Зарегистрироваться"
    PASSWORD_ERROR = (By.CSS_SELECTOR, ".input__error.text_type_main-default") #Ошибка пароля
    LOGIN_LINK = (By.CLASS_NAME, "Auth_link__1fOlj") #Гиперссылка "Войти"

class LoginPageLocators:
    EMAIL_FIELD_LOG = (By.XPATH, ".//label[text()='Email']/parent::div/input") #Поле "Email"
    PASSWORD_FIELD_LOG = (By.NAME, "Пароль") #Поле "Пароль"
    LOGIN_FORM = (By.CSS_SELECTOR, ".Auth_form__3qKeq.mb-20") #Форма входа в аккаунт
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button_button_size_medium__3zxIa") #Кнопка "Войти" на странице входа

class MainPageLocators:    #Главная страница
    AUTH_BUTTON = (By.CSS_SELECTOR, ".button_button_size_large__G21Vg") #Кнопка "Войти в аккаунт"
    PROFILE_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a") #Гиперссылка "Личный кабинет"
    ORDER_BUTTON = (By.CSS_SELECTOR, ".button_button_size_large__G21Vg") #Кнопка "Оформить заказ" (авторизован)
    CONSTRUCTOR = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2") #Конструктор

class ForgotPasswordPageLocators:
    LOGIN_LINK_FP = (By.CLASS_NAME, "Auth_link__1fOlj") #Гиперссылка "Войти"

class ProfilePageLocators:    #Личный кабинет
    PROFILE_PAGE = (By.CLASS_NAME, "Account_account__vgk_w") #Страница профиля
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/parent::a") #Гиперссылка "Конструктор"
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a") #Логотип
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']") #Кнопка "Выход"

class ConstructorLocators:    #Конструктор на главной странице
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div") #Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div") #Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div") #Раздел "Начинки"
    SECTION_SELECTED = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc") #Выбран раздел