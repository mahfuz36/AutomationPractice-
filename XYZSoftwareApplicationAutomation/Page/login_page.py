import time
from selenium.webdriver.common.by import By
from XYZSoftwareApplicationAutomation.Locators.locators import Locators
#from XYZSoftwareApplicationAutomation.HomePage import HomePage


class LoginPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.set_user = Locators.SET_USER
        self.set_password = Locators.SET_PASSWORD
        self.set_capcha = Locators.SET_CAPCHA
        self.click_login_btn = Locators.CLICK_LOGIN_BTN
        self.check_invaild_user_password_message="tblMessageContainer"

    def enter_username(self, username):
        # self.driver.get(baseUrl)
        # self.driver.get("https://training.finance.gov.bd/ibascoa2training")
        self.driver.find_element(By.ID, self.set_user).clear()
        self.driver.find_element(By.ID, self.set_user).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.set_password).clear()
        self.driver.find_element(By.ID, self.set_password).send_keys(password)

    def enter_capcha(self, capcha):
        self.driver.find_element(By.ID, self.set_capcha).clear()
        self.driver.find_element(By.ID, self.set_capcha).send_keys(capcha)

    def click_login(self):
        self.driver.find_element(By.ID, self.click_login_btn).click()

    def check_invaild_user_password_message(self):
        msg=self.driver.find_element(By.ID, self.check_invaild_user_password_message).text
        return msg
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
