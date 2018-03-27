# -*- coding:utf-8 -*-
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'esward': 'ruby',
	'phil': 'python',
	}
	
name_lists = ['jen', 'sarah', 'wushangpu', 'Tom']

for name in name_lists:
	if name.lower() in favorite_languages.keys():
		print('Thank you ' + name.title() + ' ,')
	else:
		print('Welcome to ' + name.title())
