from itertools import permutations
name = "Yars"
print [(''.join(i)).capitalize() for i in list(permutations(list(name.lower())))]