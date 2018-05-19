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

###################################################################################################
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
sleep(1)
filter = browser.find_element_by_xpath("//button[@uib-tooltip= 'Filter']")
filter.click()
sleep(3)
browser.execute_script("var a = document.getElementsByClassName('select-all ng-scope'); a[3].click(); a[3].click();")
sleep(2)
browser.execute_script("var a = document.getElementsByClassName('select-all ng-scope'); a[4].click(); a[4].click();")
sleep(2)
browser.execute_script("var a = document.getElementsByClassName('select-all ng-scope'); a[4].click(); a[4].click();")
sleep(2)
fields = browser.find_elements_by_xpath("//span[text()='Select']")
fields[-4].click()
select_sold_date = browser.find_element_by_xpath("//span[text() = 'Sold Date']")
select_sold_date.click()
browser.find_element_by_xpath("//div[@class='btn-group crm-mobile-dropdown dropdown open']").click()
sleep(1)
fields[-3].click()
f_i = browser.find_element_by_xpath("//span[text() = 'F&I']")
f_i.click()
show_room = browser.find_element_by_xpath("//span[text() = 'Showroom']")
show_room.click()
inbound_phone_call = browser.find_element_by_xpath("//span[text() = 'Inbound Phone Call']")
inbound_phone_call.click()
outbound_phone_call = browser.find_element_by_xpath("//span[text() = 'Outbound Phone Call']")
outbound_phone_call.click()
browser.find_element_by_xpath("//div[@class='btn-group crm-mobile-dropdown dropdown open']").click()
sleep(1)
fields[-2].click()
status_delivered = browser.find_element_by_xpath("//span[text()='Delivered']")
status_delivered.click()
status_sold = browser.find_element_by_xpath("//span[text()='Sold']")
status_sold.click()
browser.find_element_by_xpath("//div[@class='btn-group crm-mobile-dropdown dropdown open']").click()
sleep(1)
apply = browser.find_element_by_xpath("//button[text()='Apply']")
apply.click()

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
print(num_customers)
# for i in range(0,num_customers):
#     if (i+1)%50 == 0:
#         sleep(4)
#         print(i)
#         browser.execute_script(" var a = document.getElementsByClassName('lead-row ng-scope'); a[{}].scrollIntoView();".format(i))

for i in range(0,48):
    sleep(1)
    date_input = browser.execute_script("var a = document.getElementsByClassName('lead-row ng-scope'); b = a[{}].getElementsByClassName('lead-col lead-col-status hidden-xs ng-binding'); return b[1].innerText;".format(i))
    source_detail = browser.execute_script("var a = document.getElementsByClassName('lead-row ng-scope'); b = a[{}].getElementsByClassName('lead-col lead-col-source hidden-sm hidden-xs ng-binding'); return b[0].innerText;".format(i))
    source_detail = source_detail.strip('')
    if 'Phone Call' in source_detail:
        source_detail = 'Phone'
    print(date_input , source_detail)