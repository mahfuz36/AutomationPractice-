from selenium.webdriver.common.by import By


class Locators(object):
    # loging page objects
    BASE_URL = "https://training.finance.gov.bd/ibascoa2training"
    SET_USER = "LoginID"
    # SET_USER_ID = (By.ID, "LoginID")
    SET_PASSWORD = "Password"
    SET_CAPCHA = "Captcha"
    CLICK_LOGIN_BTN = "btnLogin"

    # SubSystem page objects
    SET_BP_XPATH = "//*[@id='ExtraLoginRequirement']/div/div[2]/button[1]"
    SET_ACC_XPATH = "//*[@id='ExtraLoginRequirement']/div/div[2]/button[2]"


    # Homepage objects
    SET_LOGOUT = "Logout"