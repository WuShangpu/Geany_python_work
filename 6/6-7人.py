# -*- coding:utf-8 -*-
my_friend = {
	'first_name': 'san',
	'last_name': 'zhang',
	'age': 24, 
	'city': 'yunnan',
	}
	
his_friend = {
	'first_name': 'si',
	'last_name': 'li',
	'age': 23, 
	'city': 'henan',
	}
	
her_friend = {
	'first_name': 'wu',
	'last_name': 'wang',
	'age': 21, 
	'city': 'hebei',
	}
	
name_lists = [my_friend, his_friend, her_friend]

for name in name_lists:
	print('\nfirst name: ' + name['first_name'])
	print('last name: ' + name['last_name'])
	print('age: ' + str(name['age']))
	print('city: ' + name['city'])
	

