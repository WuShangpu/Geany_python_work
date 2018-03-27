# -*- coding:utf-8 -*-
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'esward': 'ruby',
	'phil': 'python',
	}
	
if 'erin' not in favorite_languages.keys():
	print('Erin, please take our poll!')
	
for name in sorted(favorite_languages.keys()):
	print(name.title() + ',thank you for taking the poll.')
	
print('\n\nSarah\'s favorite language is ' + favorite_languages['sarah'].title() +\
'.')     


print('\n\nThe following languages have been mentioned:')
for language in set(favorite_languages.values()):
	print(language.title())





for name, language in favorite_languages.items():
	print(name.title() + '\'s favorite language is ' + language.title() + '.')
	
friends = ['phil', 'sarah']	
for name in favorite_languages.keys():
	print(name.title())   
	if name in friends:
		print(' Hi ' + name.title() + ' , I see your favorite language is ' + \
		favorite_languages[name].title() + '!')     
