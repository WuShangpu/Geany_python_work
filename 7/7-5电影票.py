# -*- coding:utf-8 -*-
prompt = 'How old are you? '
prompt += '\nEnter "quit" to end.'

active = True
while active:
	age = int(input(prompt))
	if age < 3:
		price = 0
	elif age >= 3 and age <=12:
		price = 10
	else:
		price = 15
				
	print('\nThe price is ' + str(price))
