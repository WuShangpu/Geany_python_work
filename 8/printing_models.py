# -*- coding:utf-8 -*-
#���ȴ���һ���б������а���һЩҪ��ӡ�����
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
#ģ���ӡÿ����ƣ�ֱ��û��δ��ӡ�����Ϊֹ
#��ӡÿ����ƺ󣬶������Ƶ��б�completed_models��
while unprinted_designs:
	current_design = unprinted_designs.pop()
	#ģ������������3D��ӡģ�͵Ĺ���
	print('Printing model: ' + current_design)
	completed_models.append(current_design)
	#��ʾ��ӡ�õ�����ģ��
print('\nThe following models have been printed:')
for completed_model in completed_models:
	print(completed_model)