# -*-coding:utf-8 -*-
names = ['zhangsan', 'lisi', 'wangmazi', 'wangwu']
countrys = ['China', 'America', 'Japan', 'Korea']
motorcycles = ['honda', 'ducati', 'suzuki', 'yamaha']

names.sort()
print(names)
names.sort(reverse=True)
print(names)

print(sorted(countrys))
print(countrys)
print(sorted(countrys,reverse=True))
print(countrys)

motorcycles.reverse()
print(motorcycles)

print(len(motorcycles))
