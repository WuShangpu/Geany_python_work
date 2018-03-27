# -*- coding:utf-8 -*-
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print('The ' + self.restaurant_name + 'is a ' + \
		self.cuisine_type + '.')
		
	def open_restaurant(self):
		print('The restaurant opens.')
		
restaurant = Restaurant('haohaochi', 'chuancai')
print('The restaurant\'s name is  ' + restaurant.restaurant_name + '.')
print('The restaurant\'s type is ' + restaurant.cuisine_type + '.')

restaurant.describe_restaurant()
restaurant.open_restaurant()
		
