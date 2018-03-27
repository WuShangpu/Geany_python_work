# -*-coding:utf-8 -*-

lists = ['zhangsan', 'lisi', 'wangwu', 'wangmazi']

print('welcome to my party, ' + lists[0] + '.')
print('welcome to my party, ' + lists[1] + '.')
print('welcome to my party, ' + lists[2] + '.')
print('welcome to my party, ' + lists[3] + '.')

print(lists[0] + 'no')

lists[0] = 'lizhiwei'
print(lists)

print('welcome to my party, ' + lists[0] + '.')
print('welcome to my party, ' + lists[1] + '.')
print('welcome to my party, ' + lists[2] + '.')
print('welcome to my party, ' + lists[3] + '.')

print('I find a bigger desk')

lists.insert(0,'haha')
lists.insert(2,'nihao')
lists.append('zhouwu')

print('welcome to my party, ' + lists[0] + '.')
print('welcome to my party, ' + lists[1] + '.')
print('welcome to my party, ' + lists[2] + '.')
print('welcome to my party, ' + lists[3] + '.')
print('welcome to my party, ' + lists[4] + '.')
print('welcome to my party, ' + lists[5] + '.')
print('welcome to my party, ' + lists[6] + '.')

print('only two')
name1 = lists.pop()
print(lists)
print(name1 + ', I am so sorry!')
name2 = lists.pop()
print(name2 + ', I am so sorry!')
name3 = lists.pop()
print(name3 + ', I am so sorry!')
name4 = lists.pop()
print(name4 + ', I am so sorry!')
name5 = lists.pop()
print(name5 + ', I am so sorry!')
print(lists)
print(lists[0] + ' nihaizai')
print(lists[1] + ' niyehazai')

del lists[0]
del lists[0]
print(lists)

