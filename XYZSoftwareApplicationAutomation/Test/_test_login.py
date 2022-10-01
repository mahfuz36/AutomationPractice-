from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
import sys
import os
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from XYZSoftwareApplicationAutomation.Page.login_page import LoginPage
from XYZSoftwareApplicationAutomation.Page.home_page import HomePage


# from Utils.param import Configuration
# from Utils import excel_utils
# from pages.signin_page import SignIn
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        time.sleep(3)

    def test_login01_valid(self):
        driver = self.driver
        driver.get("https://training.finance.gov.bd/ibascoa2training/")

        login = LoginPage(driver)
        login.enter_username('mf_cao_erd')
        login.enter_password('Bangladesh_71')
        login.enter_capcha('a1b2c')
        login.click_login()

        acc_home = HomePage(driver)
        # acc_home.click_budget_preparation()
        acc_home.click_accounting()
        acc_home.click_logout()

    def test_login02_invalid(self):
        driver = self.driver
        driver.get("https://training.finance.gov.bd/ibascoa2training/")

        login = LoginPage(driver)
        login.enter_username('mf_cao_erd')
        login.enter_password('Bangladesh_1')
        login.enter_capcha('11111')
        login.click_login()
        message = driver.find_element(By.ID, "tblMessageContainer").text
        self.assertMultiLineEqual(message, "User authentication failed.",
                                  "Please provide valid User ID, Password and Capcha")

        # acc_home = HomePage(driver)
        # # acc_home.click_budget_preparation()
        # acc_home.click_accounting()
        # acc_home.click_logout()
        """
        signin = SignIn(driver)
        signin.signin_auto_practice()

        file = 'F:\PeoplenTech QAT Course\Automationpractice\data\DataFile.xlsx'
        sheet = 'login'

        number_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            email = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            lp = LoginPage(driver)
            lp.login_auto_practice(email, password)
            print("Login Successful")
        time.sleep(3)
             
        """

        # driver.close()
        # driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('=====================')
        print("test Completed")
        print('=====================')


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="F:/PeoplenTechQATCourse/AutomationPractice/XYZSoftwareApplicationAutomation/Reports/"))
