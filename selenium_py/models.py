"""@package models
some text
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class QueryKdr:
	"""it contains data about QueryKdr"""
	def __init__(self):
		super().__init__()
		self.search_uid = ""
		self.date_request = ""
		self.status = ""
		self.zip_url = ""

class QuerySearch:
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