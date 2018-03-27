# -*- coding:utf-8 -*-
def city_country(city_name, city_coun):
	return(city_name.title() + ', ' + city_coun.title())
	
cc = city_country('beijing', 'china')
print(cc)

cc = city_country('shanghai', 'china')
print(cc)

cc = city_country('tokyo', 'japan')
print(cc)
	
