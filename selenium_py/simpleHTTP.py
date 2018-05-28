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


# sq = StatusQuery()
# sq.setUrl('5b04fd51839be764fecd2a0d','5b04fd51839be764fecd2a0e')
# sq.setPayload(1)
# sq.send()
# data = '{"location":{"status":"в обработке"}}'

# response = requests.patch('http://80.211.41.148:9999/search_queries/5b04fd51839be764fecd2a0d/locations/5b04fd51839be764fecd2a0e', headers=headers, data=data.encode('utf-8'))
# print(response.text)
# print(response.status_code)

# import json
# import requests

# class StatusQuery():
# 	"""docstring for StatusQuery"""
# 	def __init__(self):
# 		super().__init__()
# 		self.url = ""
# 		self.payload = ""

# 	def setUrl(self,id_search,id_query):
# 		self.url = "http://80.211.41.148:9999/search_queries/%s/locations/%s"%(id_search,id_query)
# 		print(self.url)

# 	def setPayload(self,status):
# 		# self.payload = '{"location":{"status":"%s"}}'%(status)
# 		self.payload = '{"loaction":{"status":"в обработке"}}'
# 		print(self.payload)

# 	def post_r(self):
# 		# r = requests.patch(self.url, data=json.dumps(self.payload))
# 		headers = {'Accept': 'application/json','Content-type': 'application/json'}
# 		# r = requests.patch(self.url, data=json.dumps(self.payload),headers=headers)
# 		r = requests.patch(self.url, data=self.payload.encode("utf-8"),headers=headers)

# 		print(r.text)
# 		print(r.status_code)
# 		print(r.request.headers)

# def sendPATCH(id_search, id_query, status):
# 	testPost = StatusQuery()
# 	testPost.setUrl(id_search,id_query)
# 	testPost.setPayload(status)
# 	testPost.post_r()

# # >>> r = requests.get(url, headers=headers)

# sendPATCH('5b04fd51839be764fecd2a0d','5b04fd51839be764fecd2a0e','готово')


#curl -v -H "Accept: application/json" -H "Content-type: application/json" -X PATCH -d '{"location":{"status":"готово"}}' http://80.211.41.148:9999/search_queries/5b04fd51839be764fecd2a0d/locations/5b04fd51839be764fecd2a0e