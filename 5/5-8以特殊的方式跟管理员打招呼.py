# -*- coding:utf-8 -*-
users_names = ['tom', 'jerry', 'admin', 'eric', 'wu']

for users_name in users_names:
	if users_name == 'admin':
		print('Hello admin,would you like to  see a status report?')
	else:
		print('Hello ' + users_name + ',' + ' thank you for logging in again')
