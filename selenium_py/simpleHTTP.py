import json
import requests

url = 'https://...'

def post_r(payload):
	r = requests.post(url, data=json.dumps(payload))
    print(r.text)
	print(r.status_code)
