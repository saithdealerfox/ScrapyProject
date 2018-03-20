# -*- coding: utf-8 -*-
import scrapy


class DominioncrmSpider(scrapy.Spider):
    name = 'dominioncrm'
    allowed_domains = ['oaklawnmazda.dominioncrm.com']
    start_urls = ['http://oaklawnmazda.dominioncrm.com/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'dantrinidad', 'password': 'dantrinidad1234'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        print('Hello ****************************************', response ,'******************************* World')
        return




# import scrapy
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from scrapy.http import Request
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as EC
# option = webdriver.ChromeOptions()
#
# option.add_argument(" — incognito")
#
# browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)
# browser.get("https://oaklawnmazda.dominioncrm.com/")
#
# username = browser.find_element_by_xpath("//input[@type='text']")
#
# username.send_keys('dantrinidad')
#
# password = browser.find_element_by_xpath("//input[@type='password']")
#
# password.send_keys('2025DMdf!')
#
# login_attempt = browser.find_element_by_xpath("//button[@class='b b-success clickable']")
#
# login_attempt.click()
#
# leads = browser.find_element_by_xpath("//a[text()='Leads']")
# leads.click()
#
# opportunity_module = browser.find_element_by_xpath("//div[@class='report--module report--module--ungrouped report--module--opportunitysourcing report--module--series--count--4 report--module--bg--undefined report--module--text--undefined report--module--text--accent--undefined']")
#
# table_rows_opp_module = opportunity_module.find_elements_by_tag_name('tr')
#
# customers = table_rows_opp_module[1].find_element_by_tag_name('td')
#
# customers.click()
#
#articles_panel = browser.find_elements_by_xpath("//div[@class='drilldowns--body']")

#articles_all = articles_panel[0].find_elements_by_tag_name('article')


# articles_count = articles_panel[0].find_elements_by_xpath("//span[@class='drilldowns--count']")

#articles_count[0].text

#articles_count[1].text



#click_article = articles_all[1].find_element_by_xpath("//header[@class='drilldown--header clickable']")

#click_article.click()