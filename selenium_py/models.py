"""@package models
some text
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

from simpleHTTP import StatusQuery as http
from collections import namedtuple

args_onHttp = False
args_onFile = False

status = ["в обработке","готово","ошибка"]

s_http = http()

"""Json to obj helper"""
def _json_object_hook(d): 
	return namedtuple('X', d.keys())(*d.values())

def jsonToobj(data): 
	return json.loads(data, object_hook=_json_object_hook)

def sendError(code,message):
	return '{"error_id":%d,"error_text":"%s"}' % (code,message)

def obj_dict(obj):
	return obj.__dict__

class QueryKdr:
	"""it contains data about QueryKdr"""
	def __init__(self):
		super().__init__()
		self.search_uid = ""
		self.date_request = ""
		self.status = ""
		self.zip_url = ""
		self.root_path = ""
	def setStatus(id_status):
		self.status = status[id_status]

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
		self.location_id=""
		self.search_uid = ""
		self.status = ""
		self.date = None
		self.date_request = None
		self.zip_url = None
		self.root_path = None
	def setStatus(self,id_status):
		self.status = status[id_status]
	def sendData(self,id_status=0):
		self.status = status[id_status]
		data = self.prepareForCS();
		print("[INFO] Send data: %s"%(data))
		if args_onHttp:
			s_http.setUrl(self.id,self.location_id)
			s_http.send(data)
		if args_onFile:
			if not os.path.exists('bin'):
				os.makedirs('bin')
			file = open('bin/result.json', 'ab')
			file.write(data.encode('utf-8'))
	def prepareForCS(self):
		q = QueryProxy()
		q.location = Sender(self.search_uid,self.status,self.root_path)
		return json.dumps(q,default=obj_dict,sort_keys=True,indent=4)

class QueryProxy:
	"""it contains data about QueryProxy"""
	def __init__(self):
		super().__init__()
	location={}

class Sender(object):
	"""docstring for Sender"""
	def __init__(self, search_uid,status,path):
		super().__init__()
		self.search_uid = search_uid
		self.status = status
		self.root_path = path

class SearchHome(object):
	"""docstring for SearchHome"""
	def __init__(self):
		super().__init__()
		self.kdastr_id = None
		self.full_address = None
		self.object_type = None
		self.area = None
		self.category = None
		self.legal_usage_type = None
		self.usage_type = None

class SearchHomeProxy:
	"""it contains data about SearchHomeProxy"""
	def __init__(self,kdastr_id):
		super().__init__()
		self.kdastr_id = kdastr_id

		

