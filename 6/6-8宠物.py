# -*- coding:utf-8 -*-
huahua = {
	'type': 'tudog',
	'host_name': 'sifa',
	}
	
doudou = {
	'type': 'tudog',
	'host_name': 'fangfang',
	}
	
pets = [huahua, doudou]

for pet in pets:
	print('pet name:' + str(pets))#���������Ĵ�ӡ����һ��������
	print('\ttype: ' + pet['type'])
	print('\thost name: ' + pet['host_name'])
