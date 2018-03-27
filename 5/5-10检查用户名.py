# -*- coding:utf-8 -*-
current_users = ['tom', 'jerry', 'admin', 'eric', 'wu']
new_users = ['Tom', 'jerry', 'eli', 'daxiong', 'jingxiang']

for new_user in new_users:
	if new_user.lower() in current_users:
		print('Please use another name.')
	else:
		print(new_user + ' could be use.')
