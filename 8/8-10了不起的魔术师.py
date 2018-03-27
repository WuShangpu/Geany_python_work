# -*- coding:utf-8 -*-


def show_magicians(magicians_name):
	for magician_name in magicians_name:
		print(magician_name)
		
		
def make_great(magicians_name):
	for magician_name in magicians_name:
		magician_name = 'The great ' + magician_name
		magicians_name.append(magician_name)
	return magicians_name
		
magicians_name = ['zhangsan', 'lisi', 'wangwu', 'wangmazi']
		
great_name = make_great(magicians_name)
print(great_name)


	
	
