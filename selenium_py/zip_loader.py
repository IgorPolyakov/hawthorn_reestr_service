"""@package zip loader
Download zip files from roseestr by job uid
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import json
import argparse

from rosreestr import Login

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import time # del

def terminate(code):
	print(code)


parser = argparse.ArgumentParser(description='Welcome to the help for zip loader v.1.')
parser.add_argument("-t", "--test", dest='onTest', action="store_true", help="For testing loader, get default values")
parser.add_argument("-T", "--token", dest='token', nargs = '?', type = str, 
	                                 default = "c5793610-b33b-476f-bebf-53a0f1366383", help="Set token for loggin on site, it's have default value.")
args = parser.parse_args()

profile = FirefoxProfile ()
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.dir", os.path.expanduser('~/download'))
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")

token = args.token.split('-')
if len(token) != 5 :
	terminate(-1)
	sys.exit("[ERROR] Wrong token") 