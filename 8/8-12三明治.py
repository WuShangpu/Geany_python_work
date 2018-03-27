# -*- coding:utf-8 -*-
def sand_toppings(*toppings):
	print('Your toppings are: ')
	for topping in toppings:
		print('- ' + topping)
		
sand_toppings('mushrooms')
sand_toppings('meat', 'milk')
sand_toppings('haha', 'hehe', 'ou')
