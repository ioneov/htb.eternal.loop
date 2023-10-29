#!/bin/python3

import zipfile
import re
import os
from os import listdir
from os.path import isfile

FILE_NAME = ''

while FILE_NAME != '6969.zip': # Because i know
	for i in listdir('.'):
		if re.match(r'[0-9]{1,7}.zip', i) != None:
			FILE_NAME = i
	with zipfile.ZipFile(FILE_NAME, 'r') as zip_file:
		for name in zip_file.namelist():
			if name != 'DoNotTouch': # Because i know
				passwd = name.split('.')[0]
				passwd = bytes(passwd, 'UTF-8')
				zip_file.extractall(pwd=passwd)
				os.remove(FILE_NAME)
