from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)
browser.set_window_size(1410,803)
browser.get("https://oaklawnmazda.dominioncrm.com/")
username = browser.find_element_by_xpath("//input[@type='text']")
username.send_keys('dantrinidad')
sleep(1)
password = browser.find_element_by_xpath("//input[@type='password']")
password.send_keys('2025DMdf!')
login_attempt = browser.find_element_by_xpath("//button[@class='b b-success clickable']")
login_attempt.click()

sleep(1)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Leads']")))
leads = browser.find_element_by_xpath("//a[text()='Leads']")
leads.click()
sleep(5)
opportunity_module = browser.find_element_by_xpath(
    "//div[@class='report--module report--module--ungrouped report--module--opportunitysourcing report--module--series--count--4 report--module--bg--undefined report--module--text--undefined report--module--text--accent--undefined']")
table_rows_opp_module = opportunity_module.find_elements_by_tag_name('tr')
customers = table_rows_opp_module[1].find_elements_by_tag_name('td')
appts_comp = customers[2]
appts_comp.click()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='drilldowns--body']")))
articles_panel = browser.find_elements_by_xpath("//div[@class='drilldowns--body']")
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='drilldowns--count']")))
articles_count = articles_panel[0].find_elements_by_xpath("//span[@class='drilldowns--count']")
num_customers = articles_count[-1].text
num_customers = int(num_customers)
scroll_times = -(-num_customers // 30) - 1
if num_customers >=30:
    for i in range(1,scroll_times+1):
        browser.execute_script(" var a =document.getElementsByTagName('article'); a[{} * 30].scrollIntoView(); ".format(i))
        sleep(3)
result_shown = {}
for i in range(0,num_customers):
    sleep(1)
    browser.execute_script("document.getElementsByClassName('drilldown--header clickable')[{}].click();".format(i))
    sleep(3)
    browser.execute_script("document.getElementsByClassName('activity--history--right')[0].scrollIntoView();")
    sleep(3)
    date_input = browser.execute_script("var ele = document.getElementsByClassName('drilldown--header clickable'); var date_input = ele[{}].getElementsByClassName('drilldown--h2  drilldown--date')[0].innerHTML ; return date_input".format(i))
    date_input = date_input.replace(',', '')
    datetime_object = datetime.strptime(date_input, '%a %b %d %Y %I:%M%p')
    date_input = datetime_object.strftime('%Y-%m-%d')
    browser.find_element_by_xpath("//span[@class='activity--history--filter--label' and text()='Lead']").click()
    source_detail=''

    if date_input not in result_shown.keys():
        result_shown[date_input] = {}
    if source_detail not in result_shown[date_input].keys():
        result_shown[date_input][source_detail] = {'S': 1}
    else:
        result_shown[date_input][source_detail]['S'] += 1
    print(date_input, source_detail)
    print('count', i)
count = -1
df = pd.DataFrame(columns=['Date', 'source_detail', 'S'])
for date_input in result_shown:
    for src in result_shown[date_input]:
        count += 1
        df.loc[count] = [date_input,
                         src,
                         result_shown[date_input][src]['S']]
print(df)
