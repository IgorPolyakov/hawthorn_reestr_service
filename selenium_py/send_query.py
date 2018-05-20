"""@package zip loader
Download zip files from roseestr by job uid
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import exit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import json

import time # del
import os


class SearchQuery:
	"""it contains data about QueryKdr"""
	def __init__(self):
		super().__init__()
		self.сadastr_id = None
		self.region = "Томская область"
		self.district = ""
		self.populated_area = ""
		self.street_type = "Улица"
		self.street_name = "Красноармейская"
		self.house_number = "148"
		self.apartment = "10"

def obj_dict(obj):
    return obj.__dict__

""" token
    *token - need get from alient app
"""

token = ["c5793610","b33b","476f","bebf","53a0f1366383"]
count_token_field = 5

s_query = SearchQuery()

browser = webdriver.Firefox()

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
	if ref_btn.text == "Поиск объектов недвижимости" :
		ref_btn.click()
		break

#this bed idea, need code refactoring
time.sleep(5);

fields = browser.find_elements_by_class_name("v-filterselect-input")
print(len(fields))
fields[0].send_keys(s_query.region)
time.sleep(2);
fields[0].send_keys(Keys.ENTER)
time.sleep(1);
fields[3].send_keys(s_query.street_type)
time.sleep(2);
fields[3].send_keys(Keys.ENTER)
time.sleep(1);

# fields1 = browser.find_elements_by_css_selector('.v-textfield.v-textfield-prompt')
# print(len(fields1))
# fields1[0].send_keys(s_query.street_name)
# time.sleep(1);

fields2 = browser.find_elements_by_class_name("v-textfield")
print(len(fields2))
fields2[1].send_keys(s_query.street_name)
time.sleep(1);
fields2[2].send_keys(s_query.house_number)
time.sleep(1);
fields2[3].send_keys(s_query.apartment)
time.sleep(5);

find_btns = browser.find_elements_by_class_name("v-button-caption")
print(len(find_btns))
for find_btn in find_btns:
	if find_btn.text == "Найти":
		find_btn.click()
		find_btn.click()
		print("Hello")
		break

time.sleep(5)

temp_table = browser.find_elements_by_class_name("v-table-row")
search_result = temp_table[0].find_elements_by_class_name("v-label")

if not search_result:
	browser.quit()
	sys.exit("don't found elemets: v-label")

search_result[0].click()

time.sleep(5)

send_request = browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div/span/span")
send_request.click()
time.sleep(5)
print("YeBATI YA LOHARA")
# find_btnss = browser.find_element_by_class_name("v-button")
# find_btnss.click()
		# v-button
# .send_keys(Keys.RETURN)

# print("***Stage 3 - parsing data")

# temp_table = browser.find_elements_by_class_name("v-table-row")

# if not ref_btns:
# 	browser.quit()
# 	sys.exit("don't found elemets: v-table-row")

# my_querys = []

# for row in temp_table:
# 	wrapper_cells = row.find_elements_by_class_name("v-table-cell-wrapper")
# 	my_query = QueryKdr()
# 	my_query.search_uid = wrapper_cells[0].text
# 	my_query.date_request = wrapper_cells[1].text
# 	labels = row.find_elements_by_css_selector('.v-label.v-label-undef-w')
# 	if labels[0].text == "Завершена":
# 		my_query.status = "done"
# 	else:
# 		my_query.status = "processing"
# 	href = row.find_element_by_xpath("//div[@class='v-link']/a")
# 	my_query.zip_url = href.get_attribute("href")
# 	my_querys.append(my_query)

# 	if my_query.search_uid == "80-39089153":
# 		href.click()
# 		time.sleep(30)

# json_string = json.dumps(my_querys,default=obj_dict,sort_keys=True,indent=4)

# time.sleep(5)

# print("***Stage 4 - process done")
# print(json_string)

# browser.quit()
