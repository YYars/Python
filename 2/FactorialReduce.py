# написать reduce, который реализует функционал факториала

from functools import reduce
def calcFact(num):
	print (reduce(lambda res, x: res*x, range(1, num+1)))
calcFact(7)