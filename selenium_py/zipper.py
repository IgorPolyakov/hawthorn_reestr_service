"""@package zipper
Download prepare zip for CS
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import subprocess
# import os.path


download_path = os.path.expanduser('~/download')
work_path = os.getcwd() + "/data/"
temp_path = os.path.expanduser('~/download/temp')
def megaZip_path(query_id):
	return work_path+query_id+"/"+query_id+".zip"

def getFilePath(query_id):
	return work_path+query_id

def getZipPath(fname):
	return download_path+"/"+fname

def reSaveZip(fname,query_id,timeout=15):
	print(getZipPath(fname))
	print(getFilePath(query_id))
	c_t = 0
	# os.chdir(download_path)
	while c_t < timeout:
		if not os.path.isfile(getZipPath(fname)):
			print("[INFO] Wait loading file...%ds!"%(c_t))
			time.sleep(2)
			c_t+=1
		else:
			break

	time.sleep(1)

	if not os.path.isfile(getZipPath(fname)):
		print("[ERROR] File not found!")
		return -1 
	
	if not os.path.exists(getFilePath(query_id)):
	    os.makedirs(getFilePath(query_id))

	r = subprocess.run(["unzip", "-o",getZipPath(fname), "-d",temp_path], stdout=subprocess.PIPE)
	r_f = r.stdout.decode('utf-8').split()
	print("[INFO] Create temp archive: "+r_f[5])
	
	result = subprocess.run(["unzip","-o", r_f[5], "-d",getFilePath(query_id)], stdout=subprocess.PIPE)
	files = result.stdout.decode('utf-8').split()
	print("[INFO] Success, result file: " +files[3])

	result = subprocess.run(["zip","-ruj", megaZip_path(query_id), files[3]], stdout=subprocess.PIPE)
	print("[INFO] Update Mega full pack zip: " +files[0])
	return files[3]

#reSaveZip("Response-80-39089138.zip","39089138")