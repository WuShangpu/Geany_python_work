# -*- coding:utf-8 -*-
def car_profile(maker, ctype, **car_info):
	profile = {}
	profile['car_maker'] = maker
	profile['car_type'] = ctype
	for key, value in car_info.items():
		profile[key] = value
	return profile
	
car = car_profile('subaru', 'outback', color='blue', tow_package=True)
print(car)
	
	
