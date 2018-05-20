"""@package zip loader
Download zip files from roseestr by job uid
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import exit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import json

import time # del
import os

import argparse
parser = argparse.ArgumentParser(description='Welcome to the help for zip loader v.1')

profile = FirefoxProfile ()
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.dir", os.path.expanduser('~/download'))
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")


class QueryKdr:
	"""it contains data about QueryKdr"""
	def __init__(self):
		super().__init__()
		self.search_uid = ""
		self.date_request = ""
		self.status = ""
		self.zip_url = ""

def obj_dict(obj):
    return obj.__dict__

# def terminator(message):
# 	sys.exit("don't found elemets:",message)


""" token
    *token - need get from alient app
"""
token = ["c5793610","b33b","476f","bebf","53a0f1366383"]
count_token_field = 5

browser = webdriver.Firefox(firefox_profile=profile)
# browser = webdriver.Firefox()

browser.get('https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn')

#this bed idea, need code refactoring
time.sleep(10)

elems = browser.find_elements_by_class_name("v-textfield")

print("***Stage 1 - load")

if not elems:
	browser.quit()
	sys.exit("don't found elemets: v-textfield")

for x in range(count_token_field):
	elems[x].send_keys(token[x])
	#this bed idea, need code refactoring
	time.sleep(1)

#this bed idea, need code refactoring
time.sleep(2)

entry_btn = browser.find_element_by_class_name("v-button-caption")

entry_btn.click()

#this bed idea, need code refactoring
time.sleep(10)

print("***Stage 2 - authorized")

ref_btns = browser.find_elements_by_class_name("v-button-caption")

if not ref_btns:
	browser.quit()
	sys.exit("don't found elemets: v-button-caption")

for ref_btn in ref_btns:
	if ref_btn.text == "Мои заявки" :
		ref_btn.click()
		break

#this bed idea, need code refactoring
time.sleep(20);

print("***Stage 3 - parsing data")

temp_table = browser.find_elements_by_class_name("v-table-row")

if not ref_btns:
	browser.quit()
	sys.exit("don't found elemets: v-table-row")

my_querys = []

for row in temp_table:
	wrapper_cells = row.find_elements_by_class_name("v-table-cell-wrapper")
	my_query = QueryKdr()
	my_query.search_uid = wrapper_cells[0].text
	my_query.date_request = wrapper_cells[1].text
	labels = row.find_elements_by_css_selector('.v-label.v-label-undef-w')
	if labels[0].text == "Завершена":
		my_query.status = "done"
	else:
		my_query.status = "processing"
	href = row.find_element_by_xpath("//div[@class='v-link']/a")
	my_query.zip_url = href.get_attribute("href")
	my_querys.append(my_query)

	if my_query.search_uid == "80-39089153":
		href.click()
		time.sleep(30)

json_string = json.dumps(my_querys,default=obj_dict,sort_keys=True,indent=4)

time.sleep(5)

print("***Stage 4 - process done")
print(json_string)


# print("***Stage 5 - start download")
# for item in my_querys:
# 	if item.status == "done":
# 		browser.get(item.zip_url)
# 		time.sleep(60)
# 		break
# print("***Stage 6 - All zip download")
# time.sleep(50)
browser.quit()
#assert 'Rosreestr' in browser.title

#elem = browser.find_element_by_name('p')  # Find the search box