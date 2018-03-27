# -*- coding:utf-8 -*-
def make_album(singer_name, album_name, sing_number = ''):
	album_info = {'singer name': singer_name, 'album name': album_name}
	if sing_number:
		album_info['sing number'] = sing_number
	return(album_info)
	
while True:
	s_name = input('Please enter the singer name: ')
	a_name = input('Please enter the album name: ')
	album = make_album(s_name, a_name)
	print(album)
	repeat = input('Would you want repeat ? yes or no ')
	if repeat == 'no':
		break



