import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs

chromedriver="C:\Drivers\selenium\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

driver.get("http://www.oddsshark.com/ncaab/lsu-alabama-odds-february-18-2017-744793")
link = driver.find_element_by_css_selector('li[id="react-tabs-2"').click()
time.sleep(1)
source = driver.page_source
soupify = bs(source, 'html.parser')

dataList = []
for ultag in soupify.find_all('ul', {'class': 'ReactTabs__TabList'}):
    print(ultag)
    for iltag in ultag.find_all('td'):
        dataList.append(iltag.get_text())
