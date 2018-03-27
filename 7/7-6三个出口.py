# -*- coding:utf-8 -*-
prompt = 'How old are you? '
prompt += '\nEnter "quit" to end.'

active = True
while active:
	age = input(prompt)
	if age == 'quit':
		break
	else:
		if int(age) >= 3 and int(age) <=12:
			price = 10
		elif int(age) > 12:
			price = 15
		elif int(age) < 3:
			price = 0
	
	print('\nThe price is ' + str(price))
