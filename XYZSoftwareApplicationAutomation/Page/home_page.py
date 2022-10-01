import time
from selenium.webdriver.common.by import By
from XYZSoftwareApplicationAutomation.Locators.locators import Locators


class HomePage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.budget_link = Locators.SET_BP_XPATH
        self.accounting_link = Locators.SET_ACC_XPATH
        self.click_logout_btn = Locators.SET_LOGOUT


    def click_budget_preparation(self):
        self.driver.find_element(By.XPATH, self.budget_link).click()

    def click_accounting(self):
        self.driver.find_element(By.XPATH, self.accounting_link).click()

    def click_logout(self):
        self.driver.find_element(By.ID, self.click_logout_btn).click()
