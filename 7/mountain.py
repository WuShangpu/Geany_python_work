# -*- coding:utf-8 -*-
responses = {}

#����һ����־��ָ�������Ƿ����
polling_active = True

while polling_active:
	#�������뱻�����ߵ����ֺͻش�
	name = input('\nWhat is your name? ')
	response = input('Which mountain would you like to climb someday? ')
	#�����洢���ֵ���
	responses[name] = response
	#�����Ƿ�����Ҫ�μӵ���
	repeat = input('Would you like to let another \
	person respond? (yes/no) ')
	if repeat == 'no':
		polling_active = False
	#�����������ʾ���
		print('\n--- Poll Results ---')
		for name, response in responses.items():
			print(name + ' would like to climb ' + response + '.')
