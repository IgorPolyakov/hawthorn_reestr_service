"""@package zip loader
Download zip files from roseestr by job uid
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import json
import argparse
import models

from rosreestr import base_url
from rosreestr import Login
from rosreestr import MainMenu
from rosreestr import ResponseMenu

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import time # del

def terminate(t,m):
	sys.exit("[%s] %s"%(t,m)) 

def obj_dict(obj):
    return obj.__dict__

parser = argparse.ArgumentParser(description='Welcome to the help for zip loader v.1.')
parser.add_argument("-t", "--test", dest='onTest', action='store_true', help="For testing loader, get default values")
parser.add_argument("-T", "--token", dest='token', nargs = '?', type = str, default = "c5793610-b33b-476f-bebf-53a0f1366383", help="Set token for loggin on site, it's have default value.")
parser.add_argument("-q", "--query", dest='query', nargs = 1, type = str, help="As a query, specify the search_uid. The query must be in the jason.")
parser.add_argument("-o","--output", dest='output', choices=["wb","file","wb&file"], default="file", help="Setup useg output type. Default: file.")

args = parser.parse_args()

profile = FirefoxProfile ()
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.dir", os.path.expanduser('~/download'))
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")

token = args.token.split('-')
if len(token) != 5 :
	terminate('ERROR','Wrong token')

browser = webdriver.Firefox(firefox_profile=profile)
browser.get(base_url)

try:
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.xpath, Login.token[0])))
    for x in range(len(token)):
		browser.find_element_by_xpath(Login.token[x]).send_keys(token[x])
		time.sleep(0.5) #for testing
except TimeoutException:
    terminate('ERROR', 'Login page was not loaded')

browser.find_element_by_xpath(Login.login_btn).click()

try:
   statement = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.xpath, MainMenu.statement)))
   statement.click()
except TimeoutException:
    terminate('ERROR', 'Main menu page was not loaded')

msg = browser.find_element_by_xpath(ResponseMenu.count_query).text
total_row = ResponseMenu.getCount(msg)
if total_row <= 0 :
	terminate('INFO','Statements are missing')


if total_row < ResponseMenu.max_row
	count_row = total_row
else
	count_row = ResponseMenu.max_row

my_querys = []
for i in xrange(1,count_row)
	my_query = QueryKdr()
	my_query.search_uid = browser.find_element_by_xpath(ResponseMenu.getTableValue(i,1)).text
	my_query.date_request = browser.find_element_by_xpath(ResponseMenu.getTableValue(i,2)).text
	my_query.status = browser.find_element_by_xpath(ResponseMenu.getTableValue(i,3)).text
	btn_load = browser.find_element_by_xpath(ResponseMenu.getTableValue(i,3))
	my_query.zip_url = btn_load.get_attribute("href")
	if my_query.search_uid == uid
		my_querys.append(my_query)
		btn_load.click()
		time.sleep(10) # for test
		#wait for download

json_string = json.dumps(my_querys,default=obj_dict,sort_keys=True,indent=4)
# upload result to app or file
# start script for repack zip task