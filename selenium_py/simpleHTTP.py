import requests

class StatusQuery():
	"""docstring for StatusQuery"""
	def __init__(self):
		super().__init__()

	headers = {
	    'Accept': 'application/json',
	    'Content-type': 'application/json',
	}

	status = ["в обработке","готово","ошибка"]

	def setUrl(self,id_search,id_query):
		self.url = "http://80.211.41.148:9999/search_queries/%s/locations/%s"%(id_search,id_query)
		print("[INFO] Send to: %s"%(self.url))

	def setPayload(self,id_status):
		self.payload = '{"location":{"status":"%s"}}' % (self.status[id_status])
		print(self.payload)

	def send(self,data):
		r = requests.patch(self.url,headers=self.headers,data=data.encode('utf-8'))
		if r.status_code == 200:
			print("[INFO] Success! Status has been set, code: %s"%(r.status_code))
		else:
			print("[WARNING] Status has not been set, error code: %s"%(r.status_code))

	def sendError(self,url,data):
		r = requests.patch(url,headers=self.headers,data=data.encode('utf-8'))
		if r.status_code == 200:
			print("[INFO] Success! Status has been set, code: %s"%(r.status_code))
		else:
			print("[WARNING] Status has not been set, error code: %s"%(r.status_code))
	
	def sendPostCustomer(self,url,data):
		r = requests.post(url,headers=self.headers,data=data.encode('utf-8'))
		if r.status_code == 200:
			print("[INFO] Success! Customer data sent, code: %s"%(r.status_code))
		else:
			print("[WARNING] Customer data has not been sent, error code: %s"%(r.status_code))

#curl -v -H "Accept: application/json" -H "Content-type: application/json" -X PATCH -d '{"location":{"status":"готово"}}' http://80.211.41.148:9999/search_queries/5b04fd51839be764fecd2a0d/locations/5b04fd51839be764fecd2a0e