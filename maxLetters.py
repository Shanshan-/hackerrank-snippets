import math, os, sys
from collections import Counter


def func(input):
    count = Counter(input)
    top = sorted(count.keys(), key=lambda x: (len(input) - count[x], x))[:3]
    for each in top:
        print(each, count[each])


tests = [[["aabbbccd"], "b a c"]]
for test in tests:
    f = func
    print(test[1], f(*test[0]))