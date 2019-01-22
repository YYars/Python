inputStr = 'Lapu kupal'
def isPalindrom(inputStr):
	tmp = ''.join(inputStr.lower().split())
	print (tmp == tmp[::-1])

isPalindrom(inputStr)