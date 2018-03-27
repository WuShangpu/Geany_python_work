# -*- coding:utf-8 -*-
rivers_country = {
	'nile': 'egypt',
	'huanghe': 'china',
	'mixixibihe': 'america',
	}
	
for river, country in rivers_country.items():
	print('The ' + river + ' runs through ' + country.title() + '.')
	print(river)
	print(country)
	
for river in rivers_country.keys():
	print('\n')
	print(river)
	
for country in rivers_country.values():
	print('\n')
	print(country.title())



