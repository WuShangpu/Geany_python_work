# -*- coding:utf-8 -*-
pizzas = ['zunbao', 'bishengke', 'bangyuehan']
friend_pizzas = pizzas[:]

pizzas.append('haha')
friend_pizzas.append('hehe')

print('My favorite pizzas are:')
for pizza in pizzas:
	print(pizza)
	
	
print('My friend\' s favorite pizza are:')
for friend_pizza in (friend_pizzas):
	print(friend_pizza)
	
