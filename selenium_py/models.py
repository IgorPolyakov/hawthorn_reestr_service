"""@package models
some text
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from collections import namedtuple

"""Json to obj helper"""
def _json_object_hook(d): 
	return namedtuple('X', d.keys())(*d.values())
def jsonToobj(data): 
	return json.loads(data, object_hook=_json_object_hook)

class QueryKdr:
	"""it contains data about QueryKdr"""
	def __init__(self):
		super().__init__()
		self.search_uid = ""
		self.date_request = ""
		self.status = ""
		self.zip_url = ""
		self.root_path = ""

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

class QueryResult:
	"""it contains data about QueryKdr"""
	def __init__(self):
		super().__init__()
		self.id = ""
		self.search_uid = ""
		self.date = ""
