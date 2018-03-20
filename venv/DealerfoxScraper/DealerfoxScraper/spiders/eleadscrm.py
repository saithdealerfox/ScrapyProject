from functools import reduce

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import scrapy
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import Request
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException




class EleadscrmSpider(scrapy.Spider):
    name = 'eleadscrm'
    allowed_domains = ['eleadcrm.com']
    start_urls = ['https://www.eleadcrm.com/evo2/fresh/login.asp']
    def start_requests(self):
        '''browser = webdriver.Remote(command_executor="http://sandel153:b1eb82d6-e29a-4ee0-a29f-a8a82ffa56d6@ondemand.saucelabs.com:80/wd/hub",
           desired_capabilities={"browserName" : "chrome",
               "platform": "Windows 10",
               "version" : "65.0",
                })'''

        src_list = {}

        ################# ------------ Spreadsheets part ------------------#################
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('clientsecret.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open("MAR").sheet1

        option = webdriver.ChromeOptions()
        option.add_argument(" — incognito")
        browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)
        browser.get("https://www.eleadcrm.com/evo2/fresh/login.asp")
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("https://www.eleadcrm.com/evo2/fresh/login.asp")
        username = browser.find_element_by_id("user")
        password = browser.find_element_by_id("password")
        username.send_keys("Dealerfox")
        password.send_keys("2017eldf1")
        login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
        login_attempt.click()
        desklog_click = browser.find_element_by_xpath("//span[@id='tdDeskLogImage']")
        desklog_click.click()

        iframe = browser.find_element_by_xpath('//iframe[contains(@id, "Main")]')
        browser.switch_to_frame(iframe)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'Filters_chkWebUps')))
        check_internet = browser.find_element_by_xpath("//input[@id='Filters_chkWebUps']")
        check_internet.click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'Filters_chkPhoneUps')))
        check_phone = browser.find_element_by_xpath("//input[@id='Filters_chkPhoneUps']")
        check_phone.click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'Filters_chkCampaignUps')))
        check_campaign = browser.find_element_by_xpath("//input[@id='Filters_chkCampaignUps']")
        check_campaign.click()


        time.sleep(10)
        num_customers = browser.find_elements_by_xpath('//table[@id="results"]/tbody/tr')
        num_customers = len(num_customers)

        for record in range(0, 5):
            if record > 0:
                iframe = browser.find_element_by_xpath('//iframe[contains(@id, "Main")]')
                browser.switch_to_frame(iframe)
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, 'DataPanel_ContentMain_CustomerName_{}'.format(record))))
            script = "document.getElementById('DataPanel_ContentMain_CustomerName_{}').scrollIntoView();".format(record)
            browser.execute_script(script)
            temp_table = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@id='DataPanel_ContentMain_CustomerName_{}']".format(record))))
            temp_table.click()
            if len(browser.window_handles) > 0:
                browser.switch_to.window(browser.window_handles[1])
                time.sleep(2)
                browser.execute_script(
                    "var i = document.getElementById('OpportunityPanel_ViewPrevOpptyLink'); if (i != null) {i.click()};")

                source_type_panel = browser.find_elements_by_xpath(
                    "//*[@id='OpportunityPanel_ActiveOpptyPanel']/table/tbody/tr[6]/td")
                source_type = source_type_panel[1].text
                source_detail_panel = browser.find_elements_by_xpath(
                    "//*[@id='OpportunityPanel_ActiveOpptyPanel']/table/tbody/tr[7]/td")
                source_detail = source_detail_panel[1].text
                if source_detail == 'Dealer Website':
                    source_detail = 'online shopper'
                if source_detail in src_list.keys():
                    src_list[source_detail]+= 1
                else:
                    src_list[source_detail] = 1

                iframe1 = browser.find_element_by_id('tabsTargetFrame')
                browser.switch_to.frame(iframe1)

                ################################################################

                oddRows = browser.find_elements_by_class_name("odd")
                evenRows = browser.find_elements_by_class_name("even")
                # print(oddRows[0].text)
                from datetime import date
                month = int(date.today().strftime("%m"))
                day = int(date.today().strftime("%d"))
                year = int(date.today().strftime("%y"))

                today = "{}/{}/{}".format(month, day, year)

                for i in oddRows:
                    s = i.text
                    s = s.split('\n')
                    s = [x for x in s if x]
                    t = [i.split(' ') for i in s]
                    if len(t) > 0:
                        import operator
                        flat_list = reduce(operator.add, t)
                        flat_list = [x for x in flat_list if x]
                        if today in flat_list and 'Complete' in flat_list[-2] and 'Edit' in flat_list[-1]:
                            if 'Appointment' in flat_list[3]:
                                print(flat_list)
                        if today in flat_list and 'View' in flat_list[-2] and 'Edit' in flat_list[-1]:
                            if 'Appointment' in flat_list[4] or 'Appointment' in flat_list[5]:
                                print(flat_list)

                        if today in flat_list and 'View' in flat_list[-2] and 'Edit' in flat_list[-1]:
                            if 'Shown' in flat_list[4] or 'Shown' in flat_list[5]:
                                print(flat_list)
                for i in evenRows:
                    s = i.text
                    s = s.split('\n')
                    s = [x for x in s if x]
                    t = [i.split(' ') for i in s]
                    if len(t) > 0:
                        import operator
                        flat_list = reduce(operator.add, t)
                        flat_list = [x for x in flat_list if x]
                        if today in flat_list and 'Complete' in flat_list[-2] and 'Edit' in flat_list[-1]:
                            if 'Appointment' in flat_list[3]:
                                print(flat_list)
                        if today in flat_list and 'View' in flat_list[-2] and 'Edit' in flat_list[-1]:
                            if 'Appointment' in flat_list[4] or 'Appointment' in flat_list[5]:
                                pass
                                #print(flat_list)

                        if today in flat_list and 'View' in flat_list[-2] and 'Edit' in flat_list[-1]:
                            if 'Shown' in flat_list[4] or 'Shown' in flat_list[5]:
                                pass
                                #print(flat_list)

                    '''div_comp_contacts = browser.find_element_by_id('gvOpptyHistory')
                    rows_cch = div_comp_contacts.find_elements_by_tag_name('tr')
                    for i in range(len(rows_cch)):
                        if i == 0:
                            if 'Sold - CRM Sold' in rows_cch[0].text:
                                rep_info = rows_cch[0].text.split(' ')
                                rep_name = rep_info[-4] + ' ' + rep_info[-3]
                                print(rep_name)
                                break
                        else:
                            if len(rows_cch[i].text.split('\n')) >= 3:
                                row_data = rows_cch[i].text
                                # print(rep_info)
                                if  'Sold - CRM Sold' in row_data:
                                     rep_info = row_data.split('\n')
                                     rep_name = rep_info[2].split(' ')
                                     rep_name = rep_name[-2]+ rep_name[-1]
                                     print(rep_name)
                                     break'''
                browser.close()
                browser.switch_to.window(browser.window_handles[0])

        print(src_list)
        return
    # def parse(self, response):
    #     #browser.quit()
    #     pass

#fromdate.send_keys(datetime.date.today().strftime("%d/%m/%Y"))
#enddate.send_keys(datetime.date.today().strftime("%d/%m/%Y"))