#!/bin/python3 

import zipfile
import re
import os
from os import listdir
from os.path import isfile

file = ''

while file != '6969.zip': # Because i know
	for i in listdir('.'):
		if re.match(r'[0-9]{1,7}.zip', i) != None:
			file = i

	with zipfile.ZipFile(file, 'r') as zip_file:
		for name in zip_file.namelist():
			if name == 'DoNotTouch': # Because i know
				pass
			else:
				passwd = name.split('.')[0]
				#passwd = re.match(r'[0-9]{1,7}', name).group()
				passwd = bytes(passwd, 'UTF-8')
				zip_file.extractall(pwd=passwd)
				os.remove(file)