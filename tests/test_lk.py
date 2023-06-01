from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import Locators


class TestStellarburgersLK:
    def test_lk_link(self, login):
        driver = login
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.PROFILE_FIELD))
        assert driver.find_element(*Locators.EXIT_BUTTON_ON_LK).text == 'Выход'

    def test_lk_constructor_logo_button(self, login):
        driver = login
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.PROFILE_FIELD))
        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.SOUS_CONSTRUCTOR_BUTTON))
        assert driver.find_element(*Locators.SOUS_CONSTRUCTOR_BUTTON).text == 'Соусы'

    def test_lk_constructor_constructor_button(self, login):
        driver = login
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.PROFILE_FIELD))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.SOUS_CONSTRUCTOR_BUTTON))
        assert driver.find_element(*Locators.SOUS_CONSTRUCTOR_BUTTON).text == 'Соусы'

    def test_lk_exit(self, login):
        driver = login
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.CHECKOUT_ORDER))
        driver.find_element(*Locators.LK_BUTTON).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.PROFILE_FIELD))
        driver.find_element(*Locators.EXIT_BUTTON_ON_LK).click()
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        assert driver.find_element(*Locators.ENTER_BUTTON_AUTH_FORM).text == 'Войти'