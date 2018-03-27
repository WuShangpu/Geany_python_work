# -*- coding:utf-8 -*-
cities = {
	'beijing':  {'country': 'china', 'population': 2000, 'fact': 'big'},
		
	'tokyo': {'country': 'japan', 'population': 1000, 'fact': 'waou'},
			
	'new_york': {'country': 'America', 'population': 3000, 'fact': 'happy'},
			
	}

for city_name, city_info in cities.items():
	print('\n' + city_name.title() + ':')
	for item, info in city_info.items():
		print('\t' + item + ':' + str(info))
		
