# -*- coding:utf-8 -*-
import build_file as bf
	
user_profile = bf.build_profile('albert', 'einstein', \
location='princeton', field='physics')
print(user_profile)

my_profile = bf.build_profile('san', 'zhang', location='chian', \
field='machine', age=24)
print(my_profile)


