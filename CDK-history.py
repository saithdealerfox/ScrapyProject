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
username = browser.find_element_by_id("UsernameTextBox")
username.send_keys('dtrinidad')
sleep(1)
password = browser.find_element_by_id("PasswordTextBox")
password.send_keys('123456')
login_attempt = browser.find_element_by_id("LogInLink")
login_attempt.click()

#****************************8 ------- User Input --------- **************************************#
start_month = 'Apr'
start_date = '1'
end_month = 'Apr'
end_date = '30'

################################################################
sleep(1)
try:
    browser.find_element_by_xpath("//button[@class='walkme-custom-balloon-button walkme-custom-balloon-normal-button walkme-custom-balloon-ok-button walkme-action-ok walkme-click-and-hover']").click()
except:
    pass
sleep(1)
try:
    browser.find_element_by_id('messageBox_button_0').click()
except:
    pass
sleep(3)
WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID,"menu-item-desk-log")))
browser.find_element_by_id('menu-item-desk-log').click()
#************************* -------- Date Filter Logic ----------**********************************#

sleep(2)
span_click = browser.find_element_by_xpath("//span[@class='input-group-addon']")
span_click.click()
month_sel = browser.find_elements_by_class_name('monthselect')
month_sel[0].click()
selected_month = month_sel[0].find_element_by_xpath("//option[text()='{}']".format(start_month))
selected_month.click()
date_sel_left = browser.find_element_by_xpath("//td[contains(@class,'available') and text() = '{}']".format(start_date))
date_sel_left.click()
month_sel = browser.find_elements_by_class_name('monthselect')
month_sel[1].click()
selected_month = month_sel[1].find_elements_by_xpath("//option[text()='{}']".format(end_month))
selected_month[1].click()
date_sel_left = browser.find_elements_by_xpath("//td[contains(@class,'available') and text() = '{}']".format(end_date))
date_sel_left[-1].click()
apply_dates = browser.find_element_by_xpath("//button[text()='Apply']")
apply_dates.click()
sleep(2)
num_customers = browser.find_element_by_xpath("//div[@class='total-result-count ng-binding']").text.split(' ')[0]
num_customers = int(num_customers)
customers = browser.find_elements_by_xpath("//div[@class='lead-row ng-scope']")
unique_customers = []
sleep(1)

# for i in range(0,num_customers):
#     if (i+1)%50 == 0:
#         sleep(4)
#         print(i)
#         browser.execute_script(" var a = document.getElementsByClassName('lead-row ng-scope'); a[{}].scrollIntoView();".format(i))
for i in range(0, 1):
    if (i+1)%50 == 0:
        sleep(3)
    browser.execute_script(" var a = document.getElementsByClassName('lead-row ng-scope'); a[{}].scrollIntoView();".format(i))
    WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='lead-customer-name hidden-xs ng-binding']")))
    customer = browser.find_elements_by_xpath("//div[@class='lead-customer-name hidden-xs ng-binding']")
    customer_name = customer[i].text
    print(customer_name)
    sleep(2)
    if customer_name in unique_customers:
        continue
    unique_customers.append(customer_name)
    browser.execute_script("var a = document.getElementsByClassName('lead-customer-name hidden-xs ng-binding'); a[{}].click(); ".format(i))
    sleep(5)
    WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//i[text()='close']")))
    close_button = browser.find_element_by_xpath("//i[text()='close']")
    close_button.click()





