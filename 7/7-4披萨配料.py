# -*- coding:utf-8 -*-
prompt = 'Please enter what you need: '
prompt += '\n(Enter \'quit\' to end.) '

active = True
while active:
	peiliao = input(prompt)
	if peiliao == 'quit':
		break
	else:
		print('we will add ' + peiliao + ' in the pizza.')
	
	
