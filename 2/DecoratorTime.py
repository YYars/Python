# функция, вычисляющая время выполнения декорируемой функции

from datetime import datetime

def benchmark(func):
    def inner(*args, **kargs):
        startTime = datetime.now()
        func(*args, **kargs)
        print(datetime.now() - startTime)
    return inner

@benchmark
def hello(who):
	print('Hello',who)

hello('human')
