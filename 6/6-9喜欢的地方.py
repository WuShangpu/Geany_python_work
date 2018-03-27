# -*- coding:utf-8 -*-
favorite_places = {
	'zhangsan': ['japan', 'America'],
	'lisi': ['China'],
	'wangwu': ['shandong', 'jinan'],
	}
	
for name, places in favorite_places.items():
	if len(places) > 1:
		print('\n' + name + '\'s favorite places are:')
		for place in places:
			print('\t' + place)
	else:
		print('\n' + name + '\'s favorite place is ' + places[0])
