from selenium import webdriver
from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)
browser.get("https://oaklawnmazda.cdkcrm.com")
# username = browser.find_element_by_id("UsernameTextBox")
# username.send_keys('dtrinidad')
# sleep(1)
# password = browser.find_element_by_id("PasswordTextBox")
# password.send_keys('2025DMdf!')
# login_attempt = browser.find_element_by_id("LogInLink")
# login_attempt.click()