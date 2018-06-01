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

import zipper
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

from pyvirtualdisplay import Display

import time # del

def terminate(t,m):
	browser.quit()
	if args.virtual:
		display.stop()
	sys.exit("[%s] %s"%(t,m))

	# if args.onHttp:
	# 	http.sendError("","") 

def obj_dict(obj):
	return obj.__dict__

parser = argparse.ArgumentParser(description='Welcome to the help for zip loader v.1.')
parser.add_argument("-v", "--virtual", dest='virtual', action='store_true', help="Enabled useg virtual display.")
parser.add_argument("-t", "--token", dest='token', nargs = '?', type = str, default = "c5793610-b33b-476f-bebf-53a0f1366383", help="Set token for loggin on site, it's have default value.")
parser.add_argument("-q", "--query", dest='query', nargs = '?', type = str, default = '[{"id":1,"location_id":1,"search_uid":"80-39089153"}]', help="As a query, specify the search_uid. The query must be in the jason.")
parser.add_argument("-f", "--file", dest='onFile', action='store_true', help="Send result to file bin/result.json.")
parser.add_argument("-http", "--http", dest='onHttp', action='store_true', help="Send result to http url.")
parser.add_argument("-o", "--output", dest='output', nargs = '?', type = str, default = "~/download", help="Set output path for download files, default ~/download.")

args = parser.parse_args()

profile = FirefoxProfile ()
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.dir", os.path.expanduser(args.output))
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")

token = args.token.split('-')
if len(token) != 5 :
	terminate('ERROR','Wrong token')

if args.onHttp:
	models.args_onHttp = True

if args.onFile:
	models.args_onFile = True

search_uids = models.jsonToobj(args.query)

if args.virtual:
	display = Display(visible=0, size=(1366, 768))
	display.start()

browser = webdriver.Firefox(firefox_profile=profile)
browser.get(base_url)

try:
	WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, Login.token[0])))
	for x in range(len(token)):
		browser.find_element_by_xpath(Login.token[x]).send_keys(token[x])
		time.sleep(0.5) #for testing
except TimeoutException:
	terminate('ERROR', 'Login page was not loaded')

browser.find_element_by_xpath(Login.login_btn).click()

try:
	statement = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, MainMenu.statement)))
	statement.click()
except TimeoutException:
	terminate('ERROR', 'Main menu page was not loaded')

try:
	msg = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, ResponseMenu.count_query)))
except TimeoutException:
	terminate('ERROR', 'Finde results page was not loaded')

total_row = ResponseMenu.getCount(msg.text)
if total_row <= 0 :
	terminate('INFO','Statements are missing')

my_querys = []
for search_uid in search_uids:
	i = 1
	my_query = models.QueryResult()
	my_query.id = search_uid.id
	my_query.location_id = search_uid.location_id
	browser.find_element_by_xpath(ResponseMenu.search_field).send_keys(search_uid.search_uid)
	browser.find_element_by_xpath(ResponseMenu.search_btn).click()

	try:
		btn_load = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, ResponseMenu.getTableValue(i,4))))
		my_query.search_uid = browser.find_element_by_xpath(ResponseMenu.getTableValue(i,1)).text
		my_query.date_request = browser.find_element_by_xpath(ResponseMenu.getTableValue(i,2)).text
		my_query.status = browser.find_element_by_xpath(ResponseMenu.getTableValue(i,3)).text
		my_query.zip_url = btn_load.get_attribute("href")
		btn_load.click()
		my_query.root_path = "%s/Response-%s.zip"%(os.path.expanduser(args.output),my_query.search_uid)
		zipper.reSaveZip("Response-%s.zip"%(my_query.search_uid),my_query.id)
		my_querys.append(my_query)
		my_query.sendData(1)
	except TimeoutException:
		print("[WARNING] ZIP file was not found!")

	browser.find_element_by_xpath(ResponseMenu.search_reset).click()
	time.sleep(1) # for test

json_string = json.dumps(my_querys,default=obj_dict,sort_keys=True,indent=4)
print(json_string)
# upload result to app or file
# start script for repack zip task

browser.quit()

if args.virtual:
	display.stop()