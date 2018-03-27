# -*- coding:utf-8 -*-
sandwich_orders = ['white_sand', 'black_sand', 'pink_sand']
finished_sandwiches = []

while sandwich_orders:
	current_sand = sandwich_orders.pop()
	print('I made your ' + current_sand + '.')
	finished_sandwiches.append(current_sand)

for sand in finished_sandwiches:
	print(sand)
	
