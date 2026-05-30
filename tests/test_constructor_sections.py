from locators import ConstructorLocators
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructorSections:
    def test_constructor_sections_select_buns_is_selected(self, logged_in_driver):
        logged_in_driver.find_element(*ConstructorLocators.SAUCES_SECTION).click() #Раздел "Соусы"
        logged_in_driver.find_element(*ConstructorLocators.BUNS_SECTION).click() #Раздел "Булки"

        buns_is_selected = WebDriverWait(logged_in_driver, 3).until(presence_of_element_located(ConstructorLocators.SECTION_SELECTED))
    
        assert buns_is_selected

    def test_constructor_sections_select_sauces_is_selected(self, logged_in_driver):
        logged_in_driver.find_element(*ConstructorLocators.SAUCES_SECTION).click() #Раздел "Соусы"

        sauces_is_selected = WebDriverWait(logged_in_driver, 3).until(presence_of_element_located(ConstructorLocators.SECTION_SELECTED))
    
        assert sauces_is_selected

    def test_constructor_sections_select_fillings_is_selected(self, logged_in_driver):
        logged_in_driver.find_element(*ConstructorLocators.FILLINGS_SECTION).click() #Раздел "Начинки"

        fillings_is_selected = WebDriverWait(logged_in_driver, 3).until(presence_of_element_located(ConstructorLocators.SECTION_SELECTED))
    
        assert fillings_is_selected
    