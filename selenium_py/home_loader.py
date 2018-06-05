"""@package zip loader
Download zip files from roseestr by job uid
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import json
import models
from simpleHTTP import StatusQuery as http
import argparse

from datetime import datetime
from collections import namedtuple

from rosreestr import base_url
from rosreestr import Login
from rosreestr import MainMenu
from rosreestr import Query
from rosreestr import Sender
from rosreestr import Search

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

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

parser = argparse.ArgumentParser(description='Welcome to the help for query sender v.1.')
parser.add_argument("-v", "--virtual", dest='virtual', action='store_true', help="Enabled useg virtual display.")
parser.add_argument("-d", "--debug", dest='debug', action='store_true', help="Disable send statement to server.")
parser.add_argument("-t", "--token", dest='token', nargs = '?', type = str, default = "c5793610-b33b-476f-bebf-53a0f1366383", help="Set token for loggin on site, it's have default value.")
parser.add_argument("-q", "--query", dest='query', nargs = '?', type = str, default = '[{"id":1,"loacation_id":1,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"19"}]',
																			help="Query for search. support only json format.")
parser.add_argument("-f", "--file", dest='onFile', action='store_true', help="Send result to file bin/send_query.json.")
parser.add_argument("-http", "--http", dest='onHttp', action='store_true', help="Send result to http url.")

args = parser.parse_args()

if args.onHttp:
	models.args_onHttp = True

if args.onFile:
	models.args_onFile = True

token = args.token.split('-')
if len(token) != 5 :
	terminate('ERROR','Wrong token')

# q_r = models.QueryResult()
# q_r.id = "5b04fd51839be764fecd2a0d"
# q_r.location_id = "5b04fd51839be764fecd2a0e"
# q_r.search_uid = "3"
# q_r.date = datetime.today().strftime("%d.%m.%Y %H:%M")
# q_r.sendData(2)
# sys.exit()
# a = models.SearchHome()
# for count in range(1,61+1):
#     setattr(a,str(count),count)
# print(json.dumps(a,default=models.obj_dict,sort_keys=True,indent=4))
# sys.exit()

# Parse JSON into an object with attributes corresponding to dict keys.
querys = models.jsonToobj(args.query)

if args.virtual:
	display = Display(visible=0, size=(1366, 768))
	display.start()

browser = webdriver.Firefox()
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
	search_estates = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, MainMenu.search_estates)))
	search_estates.click()
except TimeoutException:
	terminate('ERROR', 'Main menu page was not loaded')

query_results = []
for i in range(len(querys)):
	try:
		btn_search = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, Query.btn_search)))
	except TimeoutException:
		terminate('ERROR', 'Searh menu page was not loaded')
	#Test for one query
	if not querys[i].use_kdastr is None:
		print("do not work use_kdastr, coming soon...")

	if not querys[i].kdastr_id is None:
		print("do not work kadastr_id, coming soon...")

	if not querys[i].region is None:
		r = browser.find_element_by_xpath(Query.region)
		r.send_keys(querys[i].region)
		time.sleep(4) #for testing
		r.send_keys(Keys.ENTER)
		time.sleep(1)

	if not querys[i].district is None:
		d = browser.find_element_by_xpath(Query.district)
		d.send_keys(querys[i].district)
		time.sleep(2) #for testing
		d.send_keys(Keys.ENTER)
		time.sleep(1)

	if not querys[i].populated_area is None:
		p = browser.find_element_by_xpath(Query.populated_area)
		p.send_keys(querys[i].populated_area)
		time.sleep(2) #for testing
		p.send_keys(Keys.ENTER)
		time.sleep(1)

	if not querys[i].street_type is None:
		st = browser.find_element_by_xpath(Query.street_type)
		st.send_keys(querys[i].street_type)
		time.sleep(2) #for testing
		st.send_keys(Keys.ENTER)

	if not querys[i].street_name is None:
		browser.find_element_by_xpath(Query.street_name).send_keys(querys[i].street_name)
		time.sleep(0.5) #for testing

	if not querys[i].house_number is None:
		browser.find_element_by_xpath(Query.house_number).send_keys(str(querys[i].house_number))
		time.sleep(0.5) #for testing

	# if not querys[i].apartment is None:
	# 	browser.find_element_by_xpath(Query.apartment).send_keys(str(querys[i].apartment))
	# 	time.sleep(0.5) #for testing

	btn_search.click()
	btn_search.click()

try:
	c_r = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, Search.count_result)))
except TimeoutException:
	terminate('ERROR', 'Searh menu page was not loaded')

count_result = int (c_r.text)
if count_result <= 0:
	terminate('WARNING', 'Nothing was found at all')

for c_c in range(1,count_result+1):
	s_h = models.SearchHome()
	s_h.kdastr_id = browser.find_element_by_xpath(Search.getTableValue(c_c,1)).text
	s_h.full_address = browser.find_element_by_xpath(Search.getTableValue(c_c,2)).text
	s_h.object_type = browser.find_element_by_xpath(Search.getTableValue(c_c,3)).text
	s_h.area = browser.find_element_by_xpath(Search.getTableValue(c_c,4)).text
	s_h.category = browser.find_element_by_xpath(Search.getTableValue(c_c,5)).text
	s_h.legal_usage_type = browser.find_element_by_xpath(Search.getTableValue(c_c,6)).text
	s_h.usage_type = browser.find_element_by_xpath(Search.getTableValue(c_c,7)).text
	query_results.append(s_h)

models.send(models.prepareHome(query_results),querys[0].id)

browser.quit()

if args.virtual:
	display.stop()