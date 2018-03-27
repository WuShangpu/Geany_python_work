# -*- coding:utf-8 -*-
print('All pastrami were sold.')
sandwich_orders = ['white_sand', 'pastrami', 'black_sand', 'pink_sand', \
'pastrami', 'pastrami']

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	finished_sandwiches = sandwich_orders
	
print(finished_sandwiches)
