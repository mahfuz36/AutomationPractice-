from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from pages.accountCreate_page import NewAccountCreatePage
from pages.create_account import AccountRegistrationPage
from pages.sign_up_page import SignInAndCreate
from pages.signin_page import SignIn
from Utils.param import Configuration

class NewAccountCreate(unittest.TestCase):
    # global driver
    def new_account_create(self):
        baseUrl = Configuration.BASE_URL
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)
        time.sleep(3)

        signin = SignIn(driver)
        signin.signin_auto_practice()

        signin = SignInAndCreate(driver)
        signin.sign_up()
        time.sleep(3)
        signin.enterEmail("mah35@gmail.com")

        nwacccrt = AccountRegistrationPage(driver)
        nwacccrt.fill_in_account_registration_form(("Mr.","Md Mahfuzur","Rahman","mahfuz","ABC Ltd.","Dhaka 1207","Dhaka","12070","ABCDEF","01758050312","01758050312","DHK"))




