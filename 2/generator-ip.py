import random

def generateIP():
	l = ['.'.join([str(random.randint(0,255)) for x in range(4)])]
	yield l

print (generateIP().next())

# for x in range (10):
# 	print (generateIP().next())