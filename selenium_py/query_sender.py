"""@package zip loader
Download zip files from roseestr by job uid
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import json
import models
import argparse
import datetime

from collections import namedtuple

from rosreestr import base_url
from rosreestr import Login
from rosreestr import MainMenu
from rosreestr import Query
from rosreestr import Sender

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

def obj_dict(obj):
	return obj.__dict__

parser = argparse.ArgumentParser(description='Welcome to the help for query sender v.1.')
parser.add_argument("-v", "--virtual", dest='virtual', action='store_true', help="Enabled useg virtual display")
parser.add_argument("-t", "--token", dest='token', nargs = '?', type = str, default = "c5793610-b33b-476f-bebf-53a0f1366383", help="Set token for loggin on site, it's have default value.")
parser.add_argument("-q", "--query", dest='query', nargs = '?', type = str, const = '[{"id":1,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"17"}]',
																			required=True, help="Query for search. support only json format")
parser.add_argument("-f", "--file", dest='onFile', action='store_true', help="Send result to file bin/send_query.json")
parser.add_argument("-wb", "--websocket", dest='onWebsocket', action='store_true', help="Send result to web socket, do not work")

args = parser.parse_args()

token = args.token.split('-')
if len(token) != 5 :
	terminate('ERROR','Wrong token')

# Parse JSON into an object with attributes corresponding to dict keys.
querys = models.jsonToobj(args.query)

#if not querys[0].kdastr_id is None :
#	print("zbs")
#else:
#	print("2zbs2")
#sys.exit()

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

try:
	btn_search = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, Query.btn_search)))
except TimeoutException:
	terminate('ERROR', 'Searh menu page was not loaded')

query_results = []
i = 0
#Test for one query
if not querys[i].use_kdastr is None:
	print("do not work use_kdastr, coming soon...")

if not querys[i].kdastr_id is None:
	print("do not work kadastr_id, coming soon...")

if not querys[i].region is None:
	r = browser.find_element_by_xpath(Query.region)
	r.send_keys(querys[i].region)
	time.sleep(2) #for testing
	r.send_keys(Keys.ENTER)

if not querys[i].district is None:
	d = browser.find_element_by_xpath(Query.district)
	d.send_keys(querys[i].district)
	time.sleep(2) #for testing
	d.send_keys(Keys.ENTER)

if not querys[i].populated_area is None:
	p = browser.find_element_by_xpath(Query.populated_area)
	p.send_keys(querys[i].populated_area)
	time.sleep(2) #for testing
	p.send_keys(Keys.ENTER)

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

if not querys[i].apartment is None:
	browser.find_element_by_xpath(Query.apartment).send_keys(str(querys[i].apartment))
	time.sleep(0.5) #for testing

btn_search.click()
btn_search.click()

try:
	row = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, Sender.row_result)))
	row.click()
except TimeoutException:
	terminate('ERROR', 'Searh result page was not loaded or not found query')

try:
	btn_send = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, Sender.btn_send)))
except TimeoutException:
	terminate('ERROR', 'Somthing wrong')

main_window_handle = None
while not main_window_handle:
    main_window_handle = browser.current_window_handle

btn_send.click()
btn_send.click()

query_result = models.QueryResult()

signin_window_handle = None
while not signin_window_handle:
    for handle in browser.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break

browser.switch_to.window(signin_window_handle)
query_result.search_uid = browser.find_element_by_xpath(Sender.search_uid).text
query_result.id = querys[i].id
query_result.date = datetime.isoformat(sep='T')
query_results.append(query_result)
browser.find_element_by_xpath(Sender.btn_done).click()
browser.switch_to.window(main_window_handle) #or driver.switch_to_default_content()

try:
	retry = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, Sender.btn_new_query)))
	retry.click()
except TimeoutException:
	terminate('ERROR', 'Searh menu page was not loaded')


json_string = json.dumps(query_results,default=obj_dict,sort_keys=True,indent=4)
print(json_string)
# upload result to app or file
# start script for repack zip task

if args.onFile:
	file = open('bin/query_sender.json', 'wb')
	file.write(json_string.encode('utf-8'))

if args.onWebsocket:
	print("[INFO] This option do not work, coming soon...")

browser.quit()

if args.virtual:
	display.stop()

#[{"id":1,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"10"},{"id":1,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"10"}]
#'[{"id":1,"kdastr_id":null,"use_kdastr":false,"region":"Томская область","district":null,"populated_area":null,"street_type":"Улица","street_name":"Красноармейская","house_number":"148","apartment":"10"}]'
