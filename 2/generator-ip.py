# -*- coding: UTF-8 -*-
# генераторная функция, генерирующая случайный ip4 адрес

import random

def generateIP():
	l = ['.'.join([str(random.randint(0,255)) for x in range(4)])]
	yield l

print (generateIP().next())

# for x in range (10):
# 	print (generateIP().next())