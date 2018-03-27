# -*- coding:utf-8 -*-
def make_album(singer_name, album_name, sing_number = ''):
	album_info = {'singer name': singer_name, 'album name': album_name}
	if sing_number:
		album_info['sing number'] = sing_number
	return(album_info)
	
album1 = make_album('wangfeng', 'mingai')
print(album1)
album2 = make_album('wangfei', 'mshi')
print(album2)
album3 = make_album('zhangsn', 'lisi', 10)
print(album3)

	
