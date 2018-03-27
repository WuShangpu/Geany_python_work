# -*- coding:utf-8 -*-
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print('The ' + self.restaurant_name + ' is a ' + \
		self.cuisine_type + '.')
		
	def open_restaurant(self):
		print('The restaurant opens.')
		

restaurant1 = Restaurant('haohaochi', 'chuancai')
restaurant2 = Restaurant('henhaochi', 'yuecai')
restaurant3 = Restaurant('feichanghaochi', 'xiangcai')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

