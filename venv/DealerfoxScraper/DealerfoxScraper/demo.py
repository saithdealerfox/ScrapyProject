from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)

browser.get("https://www.eleadcrm.com/evo2/fresh/login.asp")

# Wait 20 seconds for page to load
timeout = 10
try:
   username = browser.find_element_by_id("user")
   password = browser.find_element_by_id("password")
   username.send_keys("Dealerfox")
   password.send_keys("2017eldf1")
   login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
   login_attempt.click()

except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
title = browser.title

print('title:')
print(title, '\n')

browser.close

crmsheets@scraper-crms.iam.gserviceaccount.com