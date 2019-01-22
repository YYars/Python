# сгенерировать 4 случайных ip4 адреса

import random
l = [('.'.join([str(random.randint(0,255)) for x in range(4)])) for x in range(4)]
print (l)