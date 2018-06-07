"""@package rosreestr
    map of obejct for site rosreestr
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

base_url = "https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn"

class Login():
	"""docstring for Login"""
	def __init__(self):
		super().__init__()
	token = ["/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/input",
		     "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/input",
		     "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[5]/div/input",
		     "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[7]/div/input",
		     "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[9]/div/input"]
	login_btn = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/span/span"

class MainMenu():
	"""docstring for MainMenu"""
	def __init__(self):
		super().__init__()
	statement = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/span/span"
	search_estates = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div[1]/div/div/span/span"

class ResponseMenu(object):
	"""docstring for ResponseMenu"""
	def __init__(self):
		super().__init__()
	count_query = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div"
	max_row = 25
	search_field = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/input"
	search_btn = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/span/span"
	search_reset = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/span/span"
	def getCount(text):
		count = text.split()[2]
		return int(count)		
	def getTableValue(row,col):
		if col == 1 or col == 2 :
			return "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div[2]/div[1]/table/tbody/tr[%s]/td[%s]/div"%(row,col)
		if col == 3:
			return "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div[2]/div[1]/table/tbody/tr[%s]/td[%s]/div/div/div/div[1]/div/div"%(row,col)
		if col == 4:
			return "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div[2]/div[1]/table/tbody/tr[%s]/td[%s]/div/div/a"%(row,col)

class Query():
	"""docstring for Query"""
	def __init__(self):
		super().__init__()
	kadastr = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/input"
	use_kdastr = "//*[@id=//'gwt-uid-1']"
	use_kdastr_id = "gwt-uid-1"
	region = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/input"
	district = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/input"
	district_scroll = "/html/body/div[4]/div/div[2]/table/tbody/tr[1]/td/span"
	populated_area ="/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div/input"
	street_type = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/input"
	street_name = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/input"
	house_number = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[4]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/input"
	apartment = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[4]/div/div/div/div[2]/div/div/div/div[4]/div/div/div/div[1]/div/div/div/div[1]/div/input"
	btn_search = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div/span/span"

class Search(object):
	"""docstring for Search"""
	def __init__(self):
		super().__init__()
	count_result = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[4]/div/div/div/div[1]/div/div/div/div[1]/div/div/b"
	def getTableValue(row,col):
		if col == 1:
			return "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[5]/div/div/div[2]/div[1]/table/tbody/tr[%s]/td[%s]/div/div/span"%(row,col)
		if col == 2:
			return "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[5]/div/div/div[2]/div[1]/table/tbody/tr[%s]/td[%s]/div/div"%(row,col)
		if col >=3 :
			return "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[5]/div/div/div[2]/div[1]/table/tbody/tr[%s]/td[%s]/div"%(row,col)
class Sender():
	"""docstring for Sender"""
	def __init__(self):
		super().__init__()
	row_result = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[5]/div/div/div[2]/div[1]/table/tbody/tr/td[1]/div/div"
	btn_send = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div/span/span"
	search_uid = "/html/body/div[5]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div/b"
	btn_done = "/html/body/div[5]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/span/span"
	btn_new_query = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div/span/span"
	btn_clear = "/html/body/div[1]/div[6]/div[4]/div/div/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/div/span/span"
	btn_close_popup = '//*[@id="PID511_window_close"]'