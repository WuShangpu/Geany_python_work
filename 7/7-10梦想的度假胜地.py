# -*- coding:utf-8 -*-
prompt = 'If you could visit one place in the world, \
where would you go? '  

visit_places = []

active = True
while active:
	visit_place = input(prompt)
	visit_places.append(visit_place)
	repeat = input('Would you like to let another \
	person respond? (yes/no) ')
	if repeat == 'no':
		active = False
print('visit places: ')
for vipl in visit_places:
	print('\t' + vipl)
	
	
	
