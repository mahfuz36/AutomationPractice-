from selenium.webdriver.common.by import By

from Utils.param import RegistrationPageLocators
from selenium.webdriver.support.ui import Select
import time


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class AccountRegistrationPage(BasePage):

    def fill_in_account_registration_form(self):
        gender = self.driver.find_element(*RegistrationPageLocators.MrTitle_id)
        gender_status = gender.is_selected()
        if not gender_status:
            gender.click()
        time.sleep(1)
        time.sleep(5)
        firstnam_element = self.driver.find_element(*RegistrationPageLocators.firstName_id)
        firstnam_element.send_keys('firstName_id')
        lastname_element = self.driver.find_element(*RegistrationPageLocators.lastName_id)
        lastname_element.send_keys('lastName_id')
        password_element = self.driver.find_element(*RegistrationPageLocators.password_id)
        password_element.send_keys('password_id')
        address_element = self.driver.find_element(*RegistrationPageLocators.address_id)
        address_element.send_keys('address_id')
        city_element = self.driver.find_element(*RegistrationPageLocators.city_id)
        city_element.send_keys('city_id')
        states_dropdown_element = self.driver.find_element(*RegistrationPageLocators.state_id)
        states_dropdown_element.click()

        state_select = Select(self.driver.find_element(*RegistrationPageLocators.state_id))
        state_select.select_by_visible_text('state_id')

        postal_code_element = self.driver.find_element(*RegistrationPageLocators.postalCode_id)

        phone_element = self.driver.find_element(*RegistrationPageLocators.phone_id)
        alias_element = self.driver.find_element(*RegistrationPageLocators.aliasAdress_id)
        alias_element.clear()


    def click_regiser_button(self):
        register_button_element = self.driver.find_element(*RegistrationPageLocators.register_id)
        register_button_element.click()

    def get_page_title(self):
        return self.driver.title
