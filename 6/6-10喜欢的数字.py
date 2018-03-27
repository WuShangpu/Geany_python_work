# -*- coding:utf-8 -*-
favorite_numbers = {
	'zhangsan': [1,3,5],
	'lisi': [2,4,7],
	'wangwu': [3,6,9],
	'wangmazi': [4,9,0],
	'wu': [5,6,10],
	}
	
for name, favorite_number_lists in favorite_numbers.items():
	print(name + '\'s favorite numbers are:')
	for favorite_number in favorite_number_lists:
		print('\t' + str(favorite_number))
	
