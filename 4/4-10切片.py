# -*- coding:utf-8 -*-
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('\nThe first three items in the list are:')
for the_first_three_items in players[:3]:
	print(the_first_three_items)
	
print('\nThree items from the middle of the list are:')
for middle_three in players[1:4]:
	print(middle_three)
	
print('\nThe last three items in the list are:')
for last_three in players[2:]:
	print(last_three)
