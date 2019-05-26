import os
import sys
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import csv

def scrape():
  
    chromedriver = "C:\\Drivers\\selenium\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://datatables.net/examples/basic_init/zero_configuration.html')
    link = driver.find_element_by_xpath("//*[@id='example_length']/label/select/option[4]").click()
    time.sleep(1)
    source = driver.page_source
    soupify = soup(source, "html.parser")
    datalist = []   
 
    for tabletag in soupify.find_all("table", class_="display dataTable"):
        for tdtag in tabletag.find_all("td"):
            datalist.append(tdtag.get_text())
    driver.quit()
    
    csvlist = []
    iterator = 1
    with open('test01.csv', 'w', newline='') as csvfile:
        newwriter = csv.writer(csvfile, delimiter=',')
        for index in range(len(datalist)):
            if iterator % 6 != 0:
                csvlist.append(datalist[index])
                iterator += 1
            else:
                csvlist.append(datalist[index])
                iterator += 1
                newwriter.writerow(csvlist)
                csvlist=[]
            
    from subprocess import Popen
    p = Popen('test01.csv', shell=True)
scrape()
