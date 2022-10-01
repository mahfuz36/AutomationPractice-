from selenium import webdriver
#set chromedriver.exe path
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#url launch
driver.get("https://training.finance.gov.bd/ibascoa2training")
#get page title
print('Page title: ' + driver.title)
#quit browser
driver.quit()