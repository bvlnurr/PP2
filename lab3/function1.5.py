from itertools import permutations

def string_permutations(s):
    perms = permutations(s)
    for p in perms:
        print(''.join(p))


string_permutations("abc")